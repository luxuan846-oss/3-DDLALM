import json,re,urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from lxml import html
ROOT=Path(__file__).parent
def fetch(p):
    vid=p['version_id'];path=ROOT/'raw'/f'{vid}.html'
    try:
        if not path.exists():
            req=urllib.request.Request('https://arxiv.org/html/'+vid,headers={'User-Agent':'ResearchLiteratureSurvey/1.0'})
            path.write_bytes(urllib.request.urlopen(req,timeout=35).read())
        tree=html.fromstring(path.read_bytes())
        for n in tree.xpath('//script|//style|//nav|//header|//footer'):n.drop_tree()
        for n in tree.xpath('//math'):
            alt=n.get('alttext')
            if alt:n.text=' $'+alt+'$ ';[n.remove(c) for c in list(n)]
        sections=[]
        for n in tree.xpath('//p|//h1|//h2|//h3|//h4|//h5|//table[contains(@class,"ltx_equation")]|//figcaption'):
            if n.xpath('ancestor::table[contains(@class,"ltx_equation")]'):continue
            t=re.sub(r'\s+',' ',' '.join(n.itertext())).strip()
            if t:sections.append(t)
        text='\n\n'.join(sections)
        (ROOT/'raw'/f'{vid}.txt').write_text(text)
        return vid,len(text)
    except Exception as e:return vid,str(e)
if __name__=='__main__':
    import sys
    ids=sys.argv[1:]
    rows=json.loads((ROOT/'candidates.json').read_text())
    selected=[p for p in rows if p['id'] in ids]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(fetch,selected): print(*r,flush=True)
