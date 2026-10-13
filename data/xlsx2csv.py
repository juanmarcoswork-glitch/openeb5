import zipfile, sys, os, csv, re
from xml.etree import ElementTree as ET
NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
RNS='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def col_idx(ref):
    m=re.match(r'([A-Z]+)',ref); c=0
    for ch in m.group(1): c=c*26+(ord(ch)-64)
    return c-1
def load(path,outdir):
    z=zipfile.ZipFile(path)
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        r=ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in r.findall(NS+'si'):
            shared.append(''.join(t.text or '' for t in si.iter(NS+'t')))
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    os.makedirs(outdir,exist_ok=True)
    names=[]
    for sh in wb.find(NS+'sheets'):
        nm=sh.get('name'); rid=sh.get(RNS+'id'); tgt=rels[rid]
        if not tgt.startswith('xl/'): tgt='xl/'+tgt.lstrip('/')
        root=ET.fromstring(z.read(tgt))
        rows=[]
        for row in root.iter(NS+'row'):
            cells={}
            for c in row.findall(NS+'c'):
                v=c.find(NS+'v'); t=c.get('t')
                if t=='inlineStr':
                    isx=c.find(NS+'is'); val=''.join(x.text or '' for x in isx.iter(NS+'t')) if isx is not None else ''
                elif v is None: val=''
                elif t=='s': val=shared[int(v.text)]
                else: val=v.text or ''
                cells[col_idx(c.get('r'))]=val
            if cells:
                mx=max(cells); rows.append([cells.get(i,'') for i in range(mx+1)])
            else: rows.append([])
        safe=re.sub(r'[^A-Za-z0-9_-]','_',nm)
        out=os.path.join(outdir,safe+'.csv')
        with open(out,'w',newline='',encoding='utf-8') as f:
            csv.writer(f).writerows(rows)
        names.append((nm,out,len(rows)))
    return names
for nm,out,n in load(sys.argv[1],sys.argv[2]):
    print(f'{n:5d} rows  {nm}  -> {out}')
