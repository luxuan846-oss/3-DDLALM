import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';

const root=path.dirname(fileURLToPath(import.meta.url));
const out=path.resolve(root,'../../outputs/01a10109-bdcc-7603-bedd-3d117eada104');
const {papers,stats,issues}=JSON.parse(await fs.readFile(path.join(root,'workbook_data.json'),'utf8'));
const emailPapers=JSON.parse(await fs.readFile(path.join(root,'email_arxiv_updated.json'),'utf8'));
const broadMathOC=JSON.parse(await fs.readFile(path.join(root,'broad_math_oc.json'),'utf8'));
const crossOptimization=JSON.parse(await fs.readFile(path.join(root,'cross_optimization.json'),'utf8'));
const recentRows=JSON.parse(await fs.readFile(path.join(root,'email_recent.json'),'utf8'));
const mathOCUpdates=JSON.parse(await fs.readFile(path.join(root,'../optimization_2026-09_to_2026-10-12/math_oc_updates.json'),'utf8'));
if(issues.length)throw Error(JSON.stringify(issues));
const wb=Workbook.create();
const main=wb.worksheets.add('文献总表');
const detail=wb.worksheets.add('定理核对');
const venue=wb.worksheets.add('NeurIPS 2026');
const guide=wb.worksheets.add('范围与阅读建议');
const emailSheet=wb.worksheets.add('邮箱补充');
const todaySheet=wb.worksheets.add('今日邮件整理');
const broadSheet=wb.worksheets.add('math.OC全量');
const crossSheet=wb.worksheets.add('跨分区优化候选');
const updateSheet=wb.worksheets.add('math.OC版本更新');
const navy='#20364D', muted='#596579', pale='#F2F5F8';
const nativeLinks=[];
function col(n){let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;}
function base(sh,nr,nc){
 sh.showGridLines=false;
 sh.getRangeByIndexes(0,0,nr,nc).format.font={name:'Arial',size:11,color:'#172536'};
 sh.getRangeByIndexes(0,0,nr,nc).format.verticalAlignment='top';
 sh.tabColor=navy;
}
function heading(sh,title,subtitle,last){
 sh.getRange('A2').values=[[title]];sh.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:navy};
 sh.getRange(`A2:${last}2`).format.rowHeight=27;
 sh.getRange(`A3:${last}3`).format.borders={bottom:{style:'thin',color:navy}};
 sh.getRange('A4').values=[[subtitle]];sh.getRange('A4').format.font={name:'Arial',size:11,color:muted};
 sh.getRange('A4').format.wrapText=false;
}
function fittedHeight(vals,widths,min=55){
 const lines=vals.map((v,i)=>{if(v===null||v instanceof Date)return 1;let ss=String(v);return ss.split('\n').reduce((a,line)=>a+Math.max(1,Math.ceil([...line].reduce((n,c)=>n+(c.charCodeAt(0)>255?1.7:1),0)/(widths[i]*0.93))),0);});
 return Math.min(405,Math.max(min,Math.max(...lines)*15+10));
}
function table(sh,headers,vals,widths,name,start=7){
 const end=start+vals.length, last=col(headers.length-1);
 sh.getRangeByIndexes(start-1,0,1,headers.length).values=[headers];
 if(vals.length)sh.getRangeByIndexes(start,0,vals.length,headers.length).values=vals;
 const t=sh.tables.add(`A${start}:${last}${end}`,true,name);t.style='TableStyleMedium2';t.showFilterButton=true;
 sh.getRange(`A${start}:${last}${end}`).format.wrapText=true;
 sh.getRange(`A${start}:${last}${start}`).format={fill:navy,font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:34,verticalAlignment:'center',horizontalAlignment:'center',wrapText:true};
 widths.forEach((w,i)=>sh.getRange(`${col(i)}1:${col(i)}${end}`).format.columnWidth=w);
 vals.forEach((v,i)=>sh.getRange(`A${start+1+i}:${last}${start+1+i}`).format.rowHeight=fittedHeight(v,widths));
 sh.freezePanes.freezeRows(start);sh.freezePanes.freezeColumns(2);
 return {end,last};
}
function link(sh,r,c,url,label){if(url){sh.getCell(r-1,c).values=[[label]];sh.getCell(r-1,c).format.font={name:'Arial',size:11,color:'#1760A1',underline:'single'};nativeLinks.push({sheet:sh.name,cell:`${col(c)}${r}`,url});}}
function codes(p){return [...new Set((p.comment+' '+p.abstract).match(/https?:\/\/(?:github\.com|gitlab\.com)\/[^\s)]+/g)||[])].join('\n');}
function updateField(p){
 const s=p.title+' '+p.abstract;
 const tests=[
  ['双层优化',/bilevel|hypergradient/i],['极小极大与博弈',/minimax|min-max|saddle|game|Stackelberg/i],
  ['非光滑与复合优化',/nonsmooth|non.?smooth|proximal|subgradient|weakly convex/i],
  ['约束优化与增广拉格朗日',/constraint|KKT|Lagrangian|ADMM|penalty|feasibility/i],
  ['变分不等式与不动点',/variational inequality|monotone inclusion|fixed point|extragradient/i],
  ['凸优化与加速',/convex|Frank.?Wolfe|acceleration|first.?order|second.?order/i],
  ['随机梯度与机器学习优化',/stochastic gradient|SGD|Adam|learning|neural|federated/i],
  ['在线优化与遗憾界',/online optimization|regret|bandit/i],
  ['流形与最优传输',/Riemannian|manifold|Wasserstein|optimal transport/i],
  ['零阶与高阶优化',/zeroth.?order|derivative.?free|Hessian|Newton|cubic/i],
  ['组合与离散优化',/mixed.?integer|MILP|linear programming|combinatorial|scheduling/i],
  ['控制与动态优化',/MPC|optimal control|stabilization|dynamic programming/i]
 ];
 const hits=tests.filter(([,re])=>re.test(s)).map(([name])=>name);
 return hits.slice(0,3).join('；')||'数学优化相关其他';
}
const mainHeaders=['研究领域','论文标题','算法与机制','研究问题','复杂度或速率','精度指标','计量对象与 Oracle','主要假设','发表状态','阅读优先级','首次发布日期','最近更新日期','纳入范围','核对深度','论文链接','PDF','作者','arXiv 编号','arXiv 分区','代码','DOI 或出版信息','比较注意事项','原文定位','发表状态依据'];
const mainWidths=[22,65,56,55,77,58,58,62,39,16,15,15,24,42,15,13,42,20,30,38,46,63,45,58];
const vals=papers.map(p=>[p.field,p.title,p.algorithm,p.problem,p.complexity,p.measure,p.cost,p.assumptions,p.publication,p.priority,new Date(p.published),new Date(p.updated),p.scope,p.evidence_level,'论文','PDF',p.authors.join('; '),p.version_id,p.categories.join(', '),codes(p),p.doi?'https://doi.org/'+p.doi:(p.journal_ref||'未提供 DOI / journal-ref'),p.caveat,p.evidence,p.publication_evidence]);
base(main,papers.length+8,mainHeaders.length);heading(main,'数学与机器学习优化文献','2026-09-01 至 2026-10-12 · 468 篇 · 纳入复杂度、收敛性、算法机制与数学优化相关背景；摘要条目不等于证明已验证','X');
const mt=table(main,mainHeaders,vals,mainWidths,'LiteratureTable');
main.getRange(`K8:L${mt.end}`).setNumberFormat('yyyy-mm-dd');
papers.forEach((p,i)=>{link(main,i+8,14,p.url,'arXiv');link(main,i+8,15,p.pdf,'PDF');link(main,i+8,22,p.evidence_url,p.evidence.startsWith('arXiv')?'摘要与元数据':p.evidence);});
main.getRange(`J8:J${mt.end}`).conditionalFormats.add('containsText',{text:'优先',format:{fill:'#E2EDF7',font:{bold:true,color:navy}}});
main.getRange(`N8:N${mt.end}`).conditionalFormats.add('containsText',{text:'未逐条',format:{fill:'#FFF5DD',font:{color:'#795A14'}}});

const checked=papers.filter(p=>p.anchor);
const dh=['arXiv 编号','论文标题','问题','算法','复杂度结果','精度与输出','假设与适用范围','成本核算','原文定理','比较限制','阅读意义','原文链接'];
const dw=[20,64,48,56,72,65,65,65,42,70,63,16];
const dv=checked.map(p=>[p.version_id,p.title,p.problem,p.algorithm,p.complexity,p.measure,p.assumptions,p.cost,p.evidence,p.caveat,p.relevance,'定理原文']);
base(detail,dv.length+10,dh.length);heading(detail,'定理与复杂度比较','19 篇已核对定理陈述、精度指标和主要假设；尚未完成全证明审计','L');
table(detail,dh,dv,dw,'TheoremTable');checked.forEach((p,i)=>link(detail,i+8,11,p.evidence_url,'定理原文'));

const nr=papers.filter(p=>p.publication.includes('NeurIPS 2026'));
const nh=['研究领域','论文标题','轨道','公开状态','复杂度或理论结论','关键限制','首次发布日期','作者声明原文','论文链接','核对深度'];
const nw=[22,65,18,43,78,70,16,72,16,45];
const nv=nr.map(p=>[p.field,p.title,p.track,p.publication,p.complexity,p.caveat,new Date(p.published),(p.comment+' '+p.journal_ref).trim(),'arXiv',p.evidence_level]);
base(venue,nv.length+10,nh.length);heading(venue,'NeurIPS 2026 公开录用线索','10 条主会录用声明、2 条 Workshop 声明、2 条仅标注会议；均未由官方决定逐篇确认','J');
const vt=table(venue,nh,nv,nw,'NeuripsTable');venue.getRange(`G8:G${vt.end}`).setNumberFormat('yyyy-mm-dd');nr.forEach((p,i)=>link(venue,i+8,8,p.url,'arXiv'));

const emailSubjects={
 '2608.26799':'Zhaosong Lu - new related research',
 '2608.26667':'Wotao Yin / Quoc Tran-Dinh - new related research',
 '2608.03246':'Lei Zhao - new related research',
 '2608.26688':'Yair Carmon - citation alert',
 '2608.27024':'Philippe Toint - new related research',
 '2608.27084':'Damek Davis / Yurii Nesterov - new related research',
 '2608.25557':'Daniel P. Robinson - citation alert',
 '2608.25551':'Eduard Gorbunov - new related research',
 '2608.26288':'Sen Na - citation alert'
};
const eh=['邮件日期','邮件主题','论文标题','作者','arXiv 编号','arXiv 首发日期','最近更新日期','研究分区','复杂度或理论结论','论文链接','PDF','邮箱来源','纳入说明'];
const ew=[15,45,68,38,20,16,16,27,82,15,13,24,55];
const ev=emailPapers.map(p=>[new Date((p.email_date||'2026-09-01')+'T00:00:00Z'),p.email_subject||emailSubjects[p.id]||'Google Scholar Alerts',p.title,p.authors.join('; '),p.version_id,new Date(p.published),new Date(p.updated),p.categories.join(', '),p.abstract,'arXiv','PDF',p.email_source||'Gmail: Scholar Alerts',p.email_note||'邮件命中；与公开检索结果按 arXiv 编号去重']);
base(emailSheet,ev.length+10,eh.length);heading(emailSheet,'邮箱补充','本机 Mail 中可见的 Scholar Alerts · 2026-09-01 至 2026-10-12 · 17 篇论文记录 · 指定 Gmail 尚未完成连接与全量核对','M');
const et=table(emailSheet,eh,ev,ew,'EmailTable');
emailSheet.getRange(`A8:A${et.end}`).setNumberFormat('yyyy-mm-dd');emailSheet.getRange(`F8:G${et.end}`).setNumberFormat('yyyy-mm-dd');
emailPapers.forEach((p,i)=>{link(emailSheet,i+8,9,p.url,'arXiv');link(emailSheet,i+8,10,p.pdf,'PDF');});

const th=['邮件日期','发件人/提醒','邮件主题','论文或论文组','研究方向','处理建议','备注'];
const tw=[15,23,34,82,30,18,58];
base(todaySheet,recentRows.length+10,th.length);heading(todaySheet,'今日邮件整理','本机 Mail 当前可见的 2026-10-11 至 2026-10-12 邮件摘要；指定 Gmail 尚未完成连接，因此此表不代表其完整收件箱','G');
const todayRows=recentRows;
const tt=table(todaySheet,th,todayRows,tw,'TodayMailTable');todayRows.forEach((r,i)=>todaySheet.getRange(`A${8+i}:G${8+i}`).format.rowHeight=fittedHeight(r,tw,80));
todaySheet.getRange(`F8:F${tt.end}`).conditionalFormats.add('containsText',{text:'优先',format:{fill:'#E2EDF7',font:{bold:true,color:navy}}});

const bh=['研究方向','论文标题','作者','arXiv 编号','首发日期','最近更新日期','arXiv 分区','摘要','论文链接','PDF','来源范围','说明'];
const bw=[25,68,40,20,16,16,30,105,15,13,24,44];
const bv=broadMathOC.map(p=>[p.field,p.title,p.authors.join('; '),p.version_id,new Date(p.published),new Date(p.updated),p.categories.join(', '),p.abstract,'arXiv','PDF',p.scope,p.source_note]);
base(broadSheet,bv.length+10,bh.length);heading(broadSheet,'math.OC 全量文献','2026-09-01 至 2026-10-12 · 1,269 条 arXiv math.OC 记录 · 按研究方向做宽口径归类；复杂度精读见“文献总表”','L');
const bt=table(broadSheet,bh,bv,bw,'MathOCFullTable');broadSheet.getRange(`E8:F${bt.end}`).setNumberFormat('yyyy-mm-dd');
broadMathOC.forEach((p,i)=>{link(broadSheet,i+8,8,p.url,'arXiv');link(broadSheet,i+8,9,p.pdf,'PDF');});
broadSheet.freezePanes.freezeRows(7);broadSheet.freezePanes.freezeColumns(2);

const ch=['研究方向','论文标题','作者','arXiv 编号','首次发布日期','最近更新日期','arXiv 分区','摘要','论文链接','PDF','检索范围','整理说明'];
const cw=[25,68,40,20,16,16,30,105,15,13,28,52];
const cv=crossOptimization.map(p=>[p.field,p.title,p.authors.join('; '),p.version_id,new Date(p.published),new Date(p.updated),p.categories.join(', '),p.abstract,'arXiv','PDF',p.scope,p.source_note]);
base(crossSheet,cv.length+10,ch.length);heading(crossSheet,'跨分区数学优化候选','2026-09-01 至 2026-10-12 · 3,831 条 cs.LG / stat.ML / cs.DS / math.NA 关键词候选 · 需按标题和摘要二次筛选','L');
const ct=table(crossSheet,ch,cv,cw,'CrossOptimizationTable');crossSheet.getRange(`E8:F${ct.end}`).setNumberFormat('yyyy-mm-dd');
crossOptimization.forEach((p,i)=>{link(crossSheet,i+8,8,p.url,'arXiv');link(crossSheet,i+8,9,p.pdf,'PDF');});
crossSheet.freezePanes.freezeRows(7);crossSheet.freezePanes.freezeColumns(2);

const uh=['研究方向','论文标题','作者','arXiv 编号','首次发布日期','本次版本更新日期','当前版本','arXiv 分区','摘要','论文链接','PDF','说明'];
const uw=[27,70,40,20,16,18,16,30,105,15,13,62];
const uv=mathOCUpdates.map(p=>[updateField(p),p.title,p.authors.join('; '),p.version_id,new Date(p.published),new Date(p.updated),p.version_id,p.categories.join(', '),p.abstract,'arXiv','PDF','首发早于 2026-09-01；本次版本更新发生在 2026-09-01 至 2026-10-12。宽口径版本记录，相关性需按标题与摘要筛选。']);
base(updateSheet,uv.length+10,uh.length);heading(updateSheet,'math.OC 旧文版本更新','2026-09-01 至 2026-10-12 · 749 篇首发早于窗口、期间提交新版本的 math.OC 论文 · 与近期首发分表','L');
const ut=table(updateSheet,uh,uv,uw,'MathOCUpdatesTable');
updateSheet.getRange(`E8:F${ut.end}`).setNumberFormat('yyyy-mm-dd');
mathOCUpdates.forEach((p,i)=>{link(updateSheet,i+8,9,p.url,'arXiv');link(updateSheet,i+8,10,p.pdf,'PDF');});
updateSheet.freezePanes.freezeRows(7);updateSheet.freezePanes.freezeColumns(2);

base(guide,66,8);heading(guide,'检索范围与阅读建议','检索截止日：2026-10-12；邮箱已补入 Gmail / Mail Scholar Alerts 命中论文','H');
const widths=[29,18,3,29,18,3,29,90];widths.forEach((w,i)=>guide.getRange(`${col(i)}1:${col(i)}66`).format.columnWidth=w);
guide.getRange('A7:B7').values=[['文献分组','数量']];guide.getRange('D7:E7').values=[['核对范围','数量']];
const scopeEntries=Object.entries(stats.scope||{});guide.getRangeByIndexes(7,0,scopeEntries.length,2).values=scopeEntries;
guide.getRange('A11').values=[['总计']];guide.getRange('B11').formulas=[['=SUM(B8:B10)']];
guide.getRange('D8:E10').values=[['定理陈述核对',19],['第二索引返回',128],['NeurIPS 相关线索',14]];
guide.getRange('A14:B14').values=[['研究领域','篇数']];
const fields=Object.keys(stats.fields).sort();guide.getRangeByIndexes(14,0,fields.length,1).values=fields.map(x=>[x]);
fields.forEach((f,i)=>guide.getCell(14+i,1).formulas=[[`=COUNTIF('文献总表'!$A$8:$A$${mt.end},A${15+i})`]]);
for(const range of ['A7:B7','D7:E7','A14:B14'])guide.getRange(range).format={fill:navy,font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:26};
guide.getRange('A8:E29').format.rowHeight=24;
const guidance=[
 ['纳入窗口','近期首发与旧文更新均按 2026-09-01 至 2026-10-12 记录；NeurIPS 专项可早于此窗口。日期取 arXiv 元数据。'],
 ['公开来源','arXiv math.OC 全量 1,269 条；另有跨分区 cs.LG、stat.ML、cs.DS、math.NA 的 3,831 条优化关键词候选；NeurIPS 官网时间表；第二学术索引 Deerlit。'],
 ['检索覆盖','math.OC 新增 234 条；窗口内记录含历史旧文的版本更新；跨分区候选保留宽口径结果并在专页标明需二次筛选。'],
 ['筛选边界','总表为主题筛选后的文献库，不是这些分区的全部论文。排除纯应用性能比较、无算法理论关联的图论/量子/统计复杂度文章；少量直接相关渐近或算法背景保留并注明。'],
 ['新文与版本','以 arXiv 基础编号去重，保留实际读取的最新版本号；初发日期和更新时间分列。第二索引未返回不等于文章不存在。'],
 ['核对层次','书目信息与时间窗口检查、核心定理与假设检查、索引及发表声明交叉检查分别记录。19 篇定理核对不代表 468 篇证明均已审计。'],
 ['NeurIPS 年份','官网 Paper Author Notifications 为 2026-09-24，因此最近公布录用结果的这一届按 NeurIPS 2026 整理。'],
 ['录用限制','OpenReview API 返回 403 ChallengeRequiredError；第二索引本轮未返回 NeurIPS 2026 会论文。按作者 arXiv comment/journal-ref 记录公开录用声明，未声称官方名单覆盖完整。'],
 ['邮箱进度','已整理本机 Mail 当前可见的 Scholar Alerts 与 2026-10-11 至 2026-10-12 邮件摘要，补入 17 篇论文记录。指定 Gmail 邮箱连接尚未完成，因此邮箱覆盖不完整。'],
 ['math.OC 版本更新','另列 749 篇首发早于 2026-09-01、在 2026-09-01 至 2026-10-12 期间更新的论文；与 math.OC 首发记录分开，避免混淆新论文与旧文修订。'],
 ['复杂度读法','O/Ω/Θ 分别表示上界、下界与匹配数量级；~O 等记号隐藏对数项。不同精度证书、期望/高概率、随机 oracle、维度范围必须分别比较。'],
 ['计数区别','区分外层迭代、总梯度、prox、投影、Hessian-vector、样本、通信及 regret；未知依赖明确待核对，不把每轮成本视为免费。'],
 ['优先阅读','新增重点：2610.07814（NC-PL 极小极大下界）、2610.11961（Bregman 线性化 ADMM）、2610.10927（弱拟凸优化）、2610.10495（二阶有限和下界）、2610.01843（随机双层上下界）。']
];
guide.getRange('G7:H7').values=[['项目','说明']];guide.getRange('G7:H7').format={fill:navy,font:{bold:true,color:'#FFFFFF'},rowHeight:26};
guide.getRangeByIndexes(7,6,guidance.length,2).values=guidance;guide.getRange(`G8:H${7+guidance.length}`).format.wrapText=true;
guidance.forEach((r,i)=>guide.getRange(`G${i+8}:H${i+8}`).format.rowHeight=fittedHeight(r,[29,90],55));
guide.getRange('G21').values=[['官方日期来源']];link(guide,21,7,'https://neurips.cc/Conferences/2026/Dates','NeurIPS 2026 Dates');
guide.getRange('A33').values=[['基于已核对结论的研究问题']];guide.getRange('A33').format.font={bold:true,size:14,color:navy};
const ideas=[
 ['证书与复合结构','2609.17973 / 2609.25752','已知：光滑单循环 GS 与复合多层 GS 均有 ε^(-5/2) 结果。待验证：保留可计算 prox 与固定罚参数设计时，哪些步骤支持同一复杂度。','先核对 h* 的 prox、法锥证书与 Fenchel 变换；证明一步下降式，再追踪罚参数与目标精度依赖。尚未确认新颖性。'],
 ['松弛精度与总成本','2609.39736 Cor.7、13','已知：δ 固定时 ~O(ε⁻³)，下层证书只达到 O(√(δ+ε_f))。待验证：δ 随目标精度缩小时，资格条件和罚参数如何变化。','以 g(y)=y²/2、ρ=1 检查 H_ρ(y)=y²/4；固定 δ 允许 |y|=2√δ。需要联合追踪 δ、ε_f 与内层误差。'],
 ['单循环与批量代价','2610.01843 Thm.3.1 / 2609.30501 Thm.2','已知：MRT-FD 的有限差分误差与采样方差共同决定总查询；PROBE 的外层速率不代表总调用速率。','MRT-FD：τ~ε^(1/p)、m~ε^(-2-2/p)、K~ε⁻²。PROBE：ΣK_t~T^(13/5)。仅为成本推导，尚未形成新的算法或下界。']
];
guide.getRange('A35:D35').values=[['研究问题','证据位置','已知与待验证','最小核查']];
guide.getRange('A35:D35').format={fill:navy,font:{bold:true,color:'#FFFFFF'},rowHeight:30};
// The research notes use their own wide cells on a separate row region; keep the compact counts above unchanged.
guide.getRange('A36:D38').values=ideas;
guide.getRange('A36:D38').format.wrapText=true;
guide.getRange('A36:D38').format.rowHeight=405;
// Move long research notes to G/H where the existing layout provides readable width.
guide.getRange('A33:D38').clear({applyTo:'all'});
guide.getRange('G24:H24').values=[['研究问题','依据与最小核查']];guide.getRange('G24:H24').format={fill:navy,font:{bold:true,color:'#FFFFFF'},rowHeight:30};
guide.getRange('G25:H27').values=ideas.map(x=>[x[0],x.slice(1).join('\n')]);guide.getRange('G25:H27').format.wrapText=true;
ideas.forEach((x,i)=>guide.getRange(`G${25+i}:H${25+i}`).format.rowHeight=fittedHeight([x[0],x.slice(1).join('\n')],[29,90],100));
guide.tabColor='#718096';

wb.recalculate();
const checks=await wb.inspect({kind:'table',range:'范围与阅读建议!A7:E11',include:'values,formulas',tableMaxRows:6,tableMaxCols:5,maxChars:2500});
console.log(checks.ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},summary:'final formula errors',maxChars:2000})).ndjson);
await fs.mkdir(out,{recursive:true});
const file=await SpreadsheetFile.exportXlsx(wb);await file.save(path.join(out,'优化复杂度文献_2026-09-01_2026-10-12.xlsx'));
await fs.writeFile(path.join(root,'native_links.json'),JSON.stringify(nativeLinks));
for(const [sh,range,file] of [['文献总表','A1:E10','literature_preview.png'],['定理核对','A1:E10','theorems_preview.png'],['NeurIPS 2026','A1:F10','neurips_preview.png'],['范围与阅读建议','A1:H29','scope_preview.png']]){
 try{const img=await wb.render({sheetName:sh,range,scale:1,format:'png'});await fs.writeFile(path.join(root,file),new Uint8Array(await img.arrayBuffer()));console.log('rendered',file);}catch(e){console.log('render_error',sh,e.message);}
}
await fs.writeFile(path.join(root,'verification.json'),JSON.stringify({papers:papers.length,core:checked.length,neurips:nr.length,math_oc:broadMathOC.length,cross:crossOptimization.length,email:emailPapers.length,counts:stats,inspection:checks.ndjson},null,2));
console.log('OUTPUT',path.join(out,'优化复杂度文献_2026-09-01_2026-10-12.xlsx'));
