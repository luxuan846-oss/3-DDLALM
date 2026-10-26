import json, re, time, urllib.parse
from pathlib import Path
from collect import get, parse

ROOT=Path(__file__).parent
NEW=ROOT.parent/'optimization_2026-09_to_2026-10-12'
RAW=NEW/'raw'
RAW.mkdir(parents=True,exist_ok=True)
logs=[]
def fetch(name,q,sort='submittedDate',cutoff=None):
    rows=[]; start=0; total=1
    while start<total:
        path=RAW/f'{name}_{start}.xml'
        url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode(dict(search_query=q,start=start,max_results=500,sortBy=sort,sortOrder='descending'))
        for attempt in range(3):
            try:
                body=path.read_bytes() if path.exists() else get(url)
                total,part=parse(body)
                path.write_bytes(body)
                break
            except Exception:
                if attempt==2: raise
                time.sleep(3)
        rows.extend(p for p in part if (not cutoff or p['updated'][:10]>=cutoff) and p['published'][:10]<='2026-10-12' and p['updated'][:10]<='2026-10-12')
        print(name,start,len(part),total,flush=True)
        if not part or (cutoff and part[-1]['updated'][:10]<cutoff):break
        start+=len(part);time.sleep(3)
    (RAW/f'{name}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    logs.append(dict(name=name,query=q,total=total,retrieved=len(rows),status='ok'))
    return rows

new=fetch('math_oc_increment','cat:math.OC AND submittedDate:[202610040000 TO 202610122359]')
old=json.loads((ROOT/'raw/math_oc_new.json').read_text())['rows']
updates=fetch('math_oc_updated','cat:math.OC','lastUpdatedDate','2026-09-01')
cross=fetch('cross_optimization','(cat:cs.LG OR cat:stat.ML OR cat:cs.DS OR cat:math.NA) AND (all:optimization OR all:optimisation OR all:variational OR all:bilevel OR all:proximal OR all:minimax OR all:gradient) AND submittedDate:[202609010000 TO 202610122359]')
base={p['id']:p for p in old+new}
for p in updates:
    if p['id'] in base and p['updated']>base[p['id']]['updated']:base[p['id']]=p
def save(name,data): (NEW/name).write_text(json.dumps(data,ensure_ascii=False,indent=2))
save('math_oc_new.json',list(base.values()))
save('math_oc_updates.json',[p for p in updates if p['published'][:10]<'2026-09-01'])
save('cross_candidates.json',cross)
save('search_log.json',logs)
print('TOTAL',len(base),'OLD_UPDATES',sum(p['published'][:10]<'2026-09-01' for p in updates),'CROSS',len(cross),flush=True)
