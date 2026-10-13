from pathlib import Path
import re,json
from lxml import html
ROOT=Path(__file__).parent
for path in (ROOT/'raw').glob('26*v*.html'):
    tree=html.fromstring(path.read_bytes())
    for n in tree.xpath('//math'):
        alt=n.get('alttext')
        if alt:n.text=' $'+alt+'$ ';[n.remove(c) for c in list(n)]
    claims=[]
    for n in tree.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," ltx_theorem ")]'):
        cls=n.get('class','')
        if any(k in cls.lower() for k in ['proof','lemma']):continue
        s=re.sub(r'\s+',' ',' '.join(n.itertext())).strip()
        if any(k in cls.lower() for k in ['theorem','definition','assumption','corollary','proposition']):
            claims.append({'anchor':n.get('id',''),'kind':cls,'text':s})
    (ROOT/'raw'/(path.stem+'_claims.json')).write_text(json.dumps(claims,ensure_ascii=False,indent=2))
    print(path.stem,len(claims))
