import json, re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).parent
NEWROOT = ROOT.parent / 'optimization_2026-09_to_2026-10-12'

def clean(s):
    return re.sub(r'\s+', ' ', str(s or '')).strip()

def first_sentence(s):
    s = clean(s)
    return re.split(r'(?<=[.!?])\s+', s)[0][:900]

def sentence_with(s, pat, default):
    for x in re.split(r'(?<=[.!?])\s+', clean(s)):
        if re.search(pat, x, re.I):
            return x[:1000]
    return default

def field(p):
    s = p['title'] + ' ' + p['abstract']
    tests = [
        ('双层优化', r'bilevel|hypergradient'),
        ('极小极大与博弈', r'minimax|min-max|saddle|game|Stackelberg'),
        ('非光滑与复合优化', r'nonsmooth|non.?smooth|proximal|prox|composite|subgradient|weakly convex|DC '),
        ('约束优化与增广拉格朗日', r'constraint|KKT|Lagrangian|ADMM|penalty|feasibility'),
        ('变分不等式与不动点', r'variational inequality|monotone inclusion|fixed point|extragradient|Douglas.?Rachford'),
        ('凸优化与加速', r'convex|Frank.?Wolfe|acceleration|first.?order|second.?order'),
        ('随机梯度与机器学习优化', r'stochastic gradient|SGD|Adam|learning|neural|federated'),
        ('在线优化与遗憾界', r'online optimization|regret|bandit'),
        ('流形与最优传输', r'Riemannian|manifold|Wasserstein|optimal transport'),
        ('零阶与高阶优化', r'zeroth.?order|derivative.?free|Hessian|Newton|cubic'),
        ('组合与离散优化', r'mixed.?integer|MILP|linear programming|combinatorial|scheduling|network simplex'),
        ('控制与动态优化', r'MPC|optimal control|stabilization|dynamic programming'),
    ]
    hits = [name for name, pat in tests if re.search(pat, s, re.I)]
    return '；'.join(hits[:3]) if hits else '数学优化相关其他'

def row(p, scope='近期首次发布', source='arXiv 元数据与摘要'):
    s = clean(p.get('abstract',''))
    comp = sentence_with(s, r'complexity|convergence|rate|bound|oracle|stationar|regret|iteration', '摘要未明确显式复杂度；纳入算法、收敛性或优化问题相关文献')
    alg = sentence_with(s, r'propose|introduce|develop|algorithm|method|approach', p['title'])
    priority = '优先精读' if re.search(r'complexity|lower bound|oracle|tight|optimal rate|KKT', p['title']+' '+s, re.I) else '分类阅读'
    pub = '作者提供正式发表信息' if p.get('journal_ref') else '预印本；未见公开录用声明'
    return {**p,
        'field': field(p), 'scope': scope, 'evidence_level': '摘要级整理，未逐条核对定理',
        'publication': pub, 'track': '不适用', 'publication_evidence': p.get('journal_ref') or 'arXiv；未核实是否另有正式版本',
        'problem': first_sentence(s), 'algorithm': alg, 'complexity': comp,
        'measure': sentence_with(s, r'accuracy|stationar|optimality|residual|regret|error|duality', '精度指标待按原文核对'),
        'assumptions': sentence_with(s, r'assum|smooth|convex|Lipschitz|bounded|oracle|regular', '完整假设待按原文核对'),
        'cost': sentence_with(s, r'oracle|query|gradient|sample|iteration|per round|communication', '计量对象待按原文核对'),
        'caveat': '摘要层面分类；定理、常数、维度依赖和 oracle 计量需阅读全文比较。',
        'evidence': source, 'priority': priority, 'relevance': '按数学优化主题纳入；尚未认定新的研究缺口',
        'evidence_url': p['url'], 'chinese_summary': '',
        'inclusion': '复杂度/收敛/算法理论候选' if priority == '优先精读' else '数学优化相关背景'
    }

old = json.loads((ROOT/'workbook_data.json').read_text())
papers = old['papers']
byid = {p['id']: p for p in papers}
math = json.loads((NEWROOT/'math_oc_new.json').read_text())
for p in math:
    # Keep every math.OC record in the dedicated sheet; add new records to the main table.
    if p['id'] not in byid and p['published'][:10] >= '2026-10-04':
        byid[p['id']] = row(p, '近期首次发布', 'arXiv math.OC 元数据与摘要')
    elif p['id'] in byid and p['updated'] > byid[p['id']].get('updated','') and p['published'][:10] < '2026-09-01':
        byid[p['id']] = row(p, '近期更新旧文', 'arXiv math.OC 元数据与摘要')

papers = list(byid.values())
papers.sort(key=lambda p: (0 if p.get('priority') == '优先精读' else 1, p.get('field',''), p.get('published','')), reverse=False)

broad=[]
for p in math:
    q=row(p, '近期首次发布' if p['published'][:10] >= '2026-09-01' else '近期更新旧文', 'arXiv math.OC；2026-09-01 至 2026-10-12')
    q['source_note']='arXiv math.OC；2026-09-01 至 2026-10-12；宽口径全量记录'
    broad.append(q)

cross = json.loads((NEWROOT/'cross_candidates.json').read_text())
cross_rows=[]
for p in cross:
    q=row(p, '跨分区优化候选', 'arXiv cs.LG/stat.ML/cs.DS/math.NA 关键词检索')
    q['relevance']='跨分区关键词候选；需按标题、摘要与分区人工复核'
    q['source_note']='arXiv 跨分区关键词检索；2026-09-01 至 2026-10-12'
    cross_rows.append(q)

old_email=json.loads((ROOT/'email_arxiv.json').read_text())
email_ids=['2610.11961','2610.07814','2610.08087','2609.17089','2610.10927','2610.10495','2610.10218','2610.11491']
all_meta={p['id']:p for p in math}
all_meta.update({p['id']:p for p in cross})
email_papers=[]
for p in old_email:
    email_papers.append({**p,'email_date':'2026-09-01','email_subject':'Google Scholar Alert；相关研究或引用提醒','email_source':'Mail：谷歌 / Scholar Alerts','email_note':'邮件命中；按 arXiv 编号与公开检索去重'})
for i in email_ids:
    if i in all_meta:
        p=all_meta[i]
        email_papers.append({**p,'email_date':'2026-10-11','email_subject':'Google Scholar Alert；2026-10-11 新结果或引用提醒','email_source':'Mail：谷歌 / Inbox','email_note':'邮件正文可见；arXiv 链接已补入；与公开检索按编号去重'})

email_seen=set(); email_papers=[p for p in email_papers if not (p['id'] in email_seen or email_seen.add(p['id']))]
(ROOT/'email_arxiv_updated.json').write_text(json.dumps(email_papers,ensure_ascii=False,indent=2))

today_rows=[
 ['2026-10-12','Google','账号安全提醒','luxuanli26@gmail.com 在 Windows 设备有新的登录活动','账号安全','需要本人确认','仅记录，不点击、不修改账号；Mail 读取摘要'],
 ['2026-10-12','Facebook / Reddit','社交通知','公共主页、群组推荐与 Reddit 通知','社交','一般阅读','与研究无关'],
 ['2026-10-11','Google Scholar Alerts','"nonsmooth optimization" OR "constrained optimization" 搜索提醒','2610.11961 Bregman proximal linearized ADMM；2610.10927 Weakly Quasar-Convex Optimization；2610.10495 Optimal Second-Order Algorithm；2610.10218 Hessian-Guided Wasserstein Flows；2610.11491 Lagrange multipliers','非光滑/约束/二阶/最优传输','优先阅读','邮件正文列出 2026-10-11 的相关结果；含期刊与 arXiv 混合条目'],
 ['2026-10-11','Google Scholar Alerts','Yangyang Xu 新的相关研究工作','2610.07814 SGDA is Suboptimal for Nonconvex-PL Min-Max Games；2610.08087 Logarithmic-dual-update Bregman ADMM；2609.17089 covariance matrices with parameterized metric','极小极大/ADMM/流形优化','优先阅读','含 tight complexity、最优传输与 Riemannian metric'],
 ['2026-10-11','Google Scholar Alerts','Quoc Tran-Dinh 新增引用','Strong convergence of a golden ratio proximal algorithm；Scalable first-order methods for weakly convex optimization and dynamic optimal transport；Random Reshuffling for Smooth Convex Optimization','近端/凸优化/最优传输','优先阅读','部分为正式论文或学位论文，链接按邮件原始页面保留在备注中'],
 ['2026-10-11','Google Scholar Alerts','Jiajin Li 新增引用','2610.07814 SGDA is Suboptimal；Review on robust optimization theories and applications for energy sustainability','极小极大/鲁棒优化','优先阅读','一篇 arXiv 论文与一篇综述'],
 ['2026-10-12','IKEA / Revolut','购物与金融通知','IKEA Family 邮件；Revolut 转账与账单提醒','非研究','归档阅读','未进行任何金融操作'],
 ['2026-10-12','ResearchGate / 学校通知','学术活动与网络动态','学术报告、ResearchGate 专利动态、邮件拦截提醒','其他学术信息','一般阅读','学校报告时间：2026-10-15；与优化文献分开记录'],
]
(ROOT/'email_recent.json').write_text(json.dumps(today_rows,ensure_ascii=False,indent=2))

stats=old['stats']
stats.update({
    'papers':len(papers), 'math_oc_new':len(math),
    'math_oc_increment':sum(p['published'][:10] >= '2026-10-04' for p in math),
    'math_oc_updated':sum('2026-09-01' <= p['updated'][:10] <= '2026-10-12' for p in math),
    'cross_category_candidates':len(cross_rows), 'email_paper_rows':len(email_papers),
    'as_of':'2026-10-12'
})
stats['scope']=dict(Counter(p.get('scope','未分类') for p in papers))
stats['fields']=dict(Counter(p.get('field','数学优化相关其他') for p in papers))
(ROOT/'workbook_data.json').write_text(json.dumps({'papers':papers,'stats':stats,'issues':old.get('issues',[])},ensure_ascii=False,indent=2))
(ROOT/'broad_math_oc.json').write_text(json.dumps(broad,ensure_ascii=False,indent=2))
(ROOT/'cross_optimization.json').write_text(json.dumps(cross_rows,ensure_ascii=False,indent=2))
print(json.dumps({'papers':len(papers),'math_oc':len(broad),'cross':len(cross_rows),'email':len(email_papers),'stats':stats},ensure_ascii=False,indent=2))
