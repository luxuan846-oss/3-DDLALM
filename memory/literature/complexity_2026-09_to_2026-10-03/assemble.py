import json,re,html,collections
from pathlib import Path
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'selected.json').read_text())
core=json.loads((ROOT/'core_annotations.json').read_text())
core.update(json.loads((ROOT/'extra_annotations.json').read_text()))
index={re.sub(r'v\d+$','',x['id']):x for x in json.loads((ROOT/'independent_metadata.json').read_text())}

def clean(s):
    s=html.unescape(s)
    for a,b in [('\\mathcal{O}','O'),('\\mathcal O','O'),('\\varepsilon','ε'),('\\epsilon','ε'),('\\Omega','Ω'),('\\Theta','Θ'),('\\Delta','Δ'),('\\delta','δ'),('\\sigma','σ'),('\\kappa','κ'),('\\mu','μ'),('\\lambda','λ'),('\\widetilde','~'),('\\tilde','~'),('\\left',''),('\\right',''),('\\!',''),('\\,',' '),('$','')]:s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()
def sentences(s):return re.split(r'(?<=[.!?])\s+',s)
def pick(s,pattern,default='摘要未明确；需阅读全文',cap=620):
    found=[x for x in sentences(s) if re.search(pattern,x,re.I)]
    if not found:return default
    fitting=[x for x in found if len(clean(x))<=cap]
    return clean((fitting or found)[0])
def bounds(s):
    candidates=[]
    for i,x in enumerate(sentences(s)):
        if not re.search(r'complexit|rate|bound|calls|queries|iterations|regret|convergen',x,re.I):continue
        score=0
        if '$' in x:score+=5
        if re.search(r'we (?:prove|establish|show|derive|obtain)|our (?:method|algorithm)|achiev|requires|attains|returns|yields',x,re.I):score+=5
        if re.search(r'previous|existing|prior work|best.known complexity|textbook',x,re.I):score-=5
        if len(clean(x))>850:score-=2
        candidates.append((score,-i,x))
    if not candidates:return '摘要未给出复杂度或速率；作为相关背景，定理待核对'
    return clean(max(candidates)[2])
def method(p):
    s=p['abstract'];t=p['title']
    if re.search(r'lower bound|exponential.*complexity|price of determinism',t,re.I):
        return pick(s,r'algorithm|oracle|method',default='下界研究；适用算法类需核对原文')
    return pick(s,r'we (?:propose|introduce|develop|design)|named|called|our (?:method|algorithm)|algorithm combines',default=t)
def status(p):
    v=p['comment']+' '+p['journal_ref']
    n=bool(re.search(r'neurips[\s\x27’:-]*(?:2026|26)\b|Neural Information Processing Systems.*2026',v,re.I))
    if n:
        track='Workshop' if re.search('workshop',v,re.I) else '主会线索'
        if re.search(r'accepted|to appear|to be published|version appearing|published',v,re.I) or re.search(r'NeurIPS.*2026',p['journal_ref'],re.I):
            return 'NeurIPS 2026 录用：作者公开声明',track,'arXiv comment / journal-ref；官方决定未核实'
        return 'NeurIPS 2026 会议标注；录用待核实',track,'仅有会议名称，未见明确录用声明'
    if p['journal_ref']:
        return '作者提供正式发表信息','其他期刊/会议',p['journal_ref']
    if re.search(r'accepted|to appear',v,re.I):
        return '作者注明已接收/待刊','其他期刊/会议',p['comment']
    if re.search(r'under review|submitted',v,re.I):return '预印本/在审：作者声明','不适用',p['comment']
    return '预印本；未见公开录用声明','不适用','arXiv；未核实是否另有正式版本'

VENUE_FIELDS={'2610.00911':'在线优化与遗憾界','2609.39351':'在线优化与遗憾界','2609.31940':'贝叶斯优化','2609.31107':'贝叶斯优化','2609.30856':'强化学习与策略优化','2606.21683':'随机梯度与自适应方法','2606.01708':'在线优化与遗憾界','2605.12693':'决策导向学习','2604.28144':'强化学习与策略优化','2503.06917':'零阶与高阶优化','2610.01980':'决策导向学习'}
final=[];issues=[]
for p in rows:
    s=p['abstract'];id=p['id'];c=core.get(id)
    pub,track,pubevidence=status(p)
    r={**p,'publication':pub,'track':track,'publication_evidence':pubevidence,
       'problem':clean(sentences(s)[0]),'algorithm':method(p),'complexity':bounds(s),
       'measure':pick(s,r'accuracy|stationar|optimality|suboptimality|gradient norm|residual|duality gap|regret|error',default='需按原文定义核对'),
       'assumptions':pick(s,r'under |assum|smooth|convex|Lipschitz|bounded|oracle',default='完整假设待核对'),
       'cost':pick(s,r'oracle|calls|queries|iterations|per round|regret',default='计量对象待核对'),
       'caveat':'摘要层面分类；数值界、假设与 oracle 计量须按原文比较。',
       'evidence':'arXiv 摘要、作者 comment / journal-ref',
       'evidence_level':'摘要级整理，未逐条核对定理',
       'priority':'分类阅读','relevance':'按研究领域筛选；尚未认定新的研究缺口',
       'index_check':'未被第二索引返回，不代表论文不存在',
       'evidence_url':p['url'],
       'chinese_summary':index.get(id,{}).get('mini_summary','')}
    r['field']=VENUE_FIELDS.get(id,p['field'])
    if c:
        r.update(c);r['evidence_level']='已核对定理陈述/主要假设；未完成全证明审计'
        r['priority']='优先精读';r['evidence_url']='https://arxiv.org/html/'+p['version_id']+'#'+c['anchor']
        claimfile=ROOT/'raw'/(p['version_id']+'_claims.json')
        if claimfile.exists():
            matches=[z for z in json.loads(claimfile.read_text()) if z['anchor']==c['anchor']]
            if not matches:issues.append({'id':id,'issue':'anchor missing','anchor':c['anchor']})
    if id in index:
        a=re.sub(r'\W','',p['title']).lower(); b=re.sub(r'\W','',index[id]['title']).lower()
        notation_variants={'2609.15806','2609.12785','2609.04578','2609.32195'}
        r['index_check']='第二索引标题一致' if a==b else ('第二索引标题一致；数学/重音编码不同' if id in notation_variants else '第二索引存在标题差异，保留 arXiv 当前版本')
        if a!=b and id not in notation_variants:issues.append({'id':id,'issue':'title mismatch','arxiv':p['title'],'index':index[id]['title']})
    if id in {'2609.12167','2609.28306','2609.03950','2602.16517','2512.20433','2603.28484','2609.31940','2610.01980','2609.31107','2610.01395'}:
        r['inclusion']='相关理论/算法背景；未确认为显式有限时间复杂度'
    else:r['inclusion']='复杂度/非渐近速率/上下界候选'
    if id=='2610.01980':
        r['algorithm']='一次可行集投影构建 regret 曲率近似；decision-aware scenario generation'
        r['complexity']='本文摘要给出局部二次展开及曲率近似的弱极限性质；未给出显式 ε-oracle 复杂度。30.8% 是实验改善。'
        r['caveat']='作为 NeurIPS Workshop 的相关理论背景保留；实验百分比不能当作复杂度界。'
    if id=='2609.31940':
        r['algorithm']='Hypervolume 变换扩展单目标 acquisition function；多目标 hedge 策略'
        r['complexity']='摘要主要报告算法构造与实证 sample efficiency；未给出显式 ε 或 T 的理论复杂度。'
        r['caveat']='主会录用声明与复杂度定理是不同信息；此条仅作为算法背景。'
    if id=='2609.31107':
        r['algorithm']='FITR；由后验 Fisher 信息的拉回几何构造 trust region'
        r['complexity']='摘要证明 acquisition 梯度的上界；未给出全局优化迭代/查询复杂度。'
        r['caveat']='局部梯度界不等同于达到最优解所需的查询次数；作为 BO 理论背景。'
    final.append(r)

final.sort(key=lambda x:(0 if x['id'] in core else 1, x['field'], -int(x['updated'][:10].replace('-',''))))
stats={'papers':len(final),'theorem_checked':len(core),'index_returned':sum(x['id'] in index for x in final),
 'fields':dict(collections.Counter(x['field'] for x in final)), 'scope':dict(collections.Counter(x['scope'] for x in final)),
 'neurips':dict(collections.Counter(x['publication']+' / '+x['track'] for x in final if 'NeurIPS 2026' in x['publication'])),
 'math_oc_new':1035,'cross_category_new':2766,'recent_math_oc_updated':772,'updated_older':290}
(ROOT/'workbook_data.json').write_text(json.dumps({'papers':final,'stats':stats,'issues':issues},ensure_ascii=False,indent=2))
print(json.dumps(stats,ensure_ascii=False,indent=2)); print('issues',json.dumps(issues,ensure_ascii=False))
