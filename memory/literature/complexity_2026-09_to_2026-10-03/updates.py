from collect import get,parse,ROOT,RAW
import json,urllib.parse,time
q='cat:math.OC AND (all:complexity OR all:stationary OR all:oracle OR all:convergence)'
rows=[]
for start in range(0,4000,500):
    url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'start':start,'max_results':500,'sortBy':'lastUpdatedDate','sortOrder':'descending'})
    path=RAW/f'actual_updates_{start}.xml'
    try:
        b=path.read_bytes() if path.exists() else get(url);path.write_bytes(b)
        total,part=parse(b)
        keep=[x for x in part if '2026-09-01'<=x['updated'][:10]<='2026-10-03']
        rows+=keep
        print(start,len(part),'in window',len(keep),'oldest',part[-1]['updated'] if part else '',flush=True)
        if not part or part[-1]['updated'][:10]<'2026-09-01':break
        time.sleep(3)
    except Exception as e:print(str(e),flush=True);break
(ROOT/'updates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('old revised papers',sum(x['published'][:10]<'2026-09-01' for x in rows),flush=True)
