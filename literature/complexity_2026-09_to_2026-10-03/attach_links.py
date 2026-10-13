"""Add native worksheet hyperlinks, unsupported by the artifact renderer/formula engine."""
import json,zipfile,posixpath,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).parent
target=ROOT.parent.parent/'outputs/01a10109-bdcc-7603-bedd-3d117eada104/优化复杂度文献_2026-09-01_2026-10-12.xlsx'
links=json.loads((ROOT/'native_links.json').read_text())
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
rel='http://schemas.openxmlformats.org/package/2006/relationships'
rns='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
ET.register_namespace('',ns);ET.register_namespace('r',rns)
with zipfile.ZipFile(target) as z:files={n:z.read(n) for n in z.namelist()}
work=ET.fromstring(files['xl/workbook.xml']);rels=ET.fromstring(files['xl/_rels/workbook.xml.rels'])
targets={r.get('Id'):r.get('Target') for r in rels}
for sheet in work.find('{'+ns+'}sheets'):
    wanted=[l for l in links if l['sheet']==sheet.get('name')]
    if not wanted:continue
    st=targets[sheet.get('{'+rns+'}id')]
    filename=st.lstrip('/') if st.startswith('/') else posixpath.normpath(posixpath.join('xl',st))
    tree=ET.fromstring(files[filename]);h=ET.Element('{'+ns+'}hyperlinks')
    relpath=posixpath.join(posixpath.dirname(filename),'_rels',posixpath.basename(filename)+'.rels')
    sr=ET.fromstring(files[relpath]) if relpath in files else ET.Element('{'+rel+'}Relationships')
    used={r.get('Id') for r in sr};counter=1
    for l in wanted:
        while f'rIdHyperlink{counter}' in used:counter+=1
        rid=f'rIdHyperlink{counter}';used.add(rid);counter+=1
        ET.SubElement(h,'{'+ns+'}hyperlink',{'ref':l['cell'],'{'+rns+'}id':rid})
        ET.SubElement(sr,'{'+rel+'}Relationship',{'Id':rid,'Type':rns+'/hyperlink','Target':l['url'],'TargetMode':'External'})
    # Hyperlinks follow data validations and precede print/drawing/table elements.
    after={'printOptions','pageMargins','pageSetup','headerFooter','rowBreaks','colBreaks','customProperties','cellWatches','ignoredErrors','smartTags','drawing','legacyDrawing','legacyDrawingHF','picture','oleObjects','controls','webPublishItems','tableParts','extLst'}
    at=next((i for i,c in enumerate(tree) if c.tag.split('}')[-1] in after),len(tree))
    tree.insert(at,h)
    files[filename]=ET.tostring(tree,encoding='utf-8',xml_declaration=True)
    files[relpath]=ET.tostring(sr,encoding='utf-8',xml_declaration=True)
temp=target.with_suffix('.tmp.xlsx')
with zipfile.ZipFile(temp,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for n,b in files.items():z.writestr(n,b)
temp.replace(target)
print('Native hyperlinks added:',len(links))
