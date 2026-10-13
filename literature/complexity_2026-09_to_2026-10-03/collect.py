import json, re, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).parent
RAW = ROOT / 'raw'
NS = {'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
DATE = 'submittedDate:[202609010000 TO 202610032359]'
CATS = '(cat:math.OC OR cat:cs.LG OR cat:stat.ML OR cat:cs.DS OR cat:math.NA)'
KEYS = '(all:complexity OR all:stationary OR all:convergence OR all:regret OR all:minimax OR all:bilevel OR all:gradient OR all:oracle)'
QUERIES = {
 'math_oc_new': 'cat:math.OC AND '+DATE,
 'ml_algorithms_new': CATS+' AND '+KEYS+' AND '+DATE,
 'optimization_updates': CATS+' AND '+KEYS+' AND lastUpdatedDate:[202609010000 TO 202610032359]',
 'neurips_2026': '(all:NeurIPS OR all:NIPS) AND all:2026 AND '+CATS+' AND '+KEYS,
}
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'ResearchLiteratureSurvey/1.0'})
    return urllib.request.urlopen(req,timeout=50).read()
def parse(body):
    root=ET.fromstring(body)
    rows=[]
    for e in root.findall('a:entry',NS):
        def t(k): return re.sub(r'\s+',' ',e.findtext(k,default='',namespaces=NS)).strip()
        full=t('a:id').split('/abs/')[-1]
        if not re.match(r'\d{4}\.\d+',full):continue
        rows.append({'id':re.sub(r'v\d+$','',full),'version_id':full,'title':t('a:title'),'abstract':t('a:summary'),'published':t('a:published'),'updated':t('a:updated'),'authors':[a.findtext('a:name',namespaces=NS) for a in e.findall('a:author',NS)],'categories':[c.attrib['term'] for c in e.findall('a:category',NS)],'comment':t('x:comment'),'journal_ref':t('x:journal_ref'),'doi':t('x:doi'),'url':'https://arxiv.org/abs/'+full,'pdf':'https://arxiv.org/pdf/'+full})
    return int(root.findtext('o:totalResults',default='0',namespaces=NS)),rows
def collect(name,q):
    allrows=[]; start=0; total=1
    while start<total:
        url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'start':start,'max_results':500,'sortBy':'submittedDate','sortOrder':'descending'})
        path=RAW/f'{name}_{start}.xml'
        body=path.read_bytes() if path.exists() else get(url)
        path.write_bytes(body)
        total,rows=parse(body);allrows+=rows
        print(name,start,len(rows),'total',total,flush=True)
        if not rows:break
        start+=len(rows)
        time.sleep(3)
    (RAW/f'{name}.json').write_text(json.dumps({'query':q,'total':total,'rows':allrows},ensure_ascii=False,indent=2))
    return name,allrows
if __name__=='__main__':
    merged={}; logs=[]
    for name,q in QUERIES.items():
        try:
            name,rows=collect(name,q)
            for p in rows:
                if p['id'] not in merged:merged[p['id']]={**p,'sources':[]}
                merged[p['id']]['sources'].append(name)
            logs.append({'name':name,'query':q,'count':len(rows),'status':'ok'})
        except Exception as e:
            logs.append({'name':name,'query':q,'status':'failed','error':str(e)}); print(name,str(e),flush=True)
    (ROOT/'candidates.json').write_text(json.dumps(list(merged.values()),ensure_ascii=False,indent=2))
    (ROOT/'search_log.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
    print('UNIQUE',len(merged),flush=True)
