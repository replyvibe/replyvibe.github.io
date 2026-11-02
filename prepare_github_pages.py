from pathlib import Path
import re,os,shutil
root=Path('.');src=Path('dist')
for p in src.rglob('*'):
 if not p.is_file():continue
 rel=p.relative_to(src);out=root/rel;out.parent.mkdir(parents=True,exist_ok=True)
 if p.suffix=='.html':
  s=p.read_text(encoding='utf-8')
  def link(m):
   attr,url=m.group(1),m.group(2)
   if not url.startswith('/') or url.startswith('//'):return m.group(0)
   path,sep,frag=url.partition('#');target=path.lstrip('/') or 'index.html'
   value=os.path.relpath(target,str(rel.parent)).replace('\\','/')
   return attr+'="'+value+('#'+frag if sep else '')+'"'
  s=re.sub(r'(href|src)="([^"]*)"',link,s)
  out.write_text(s,encoding='utf-8')
 else:shutil.copy2(p,out)
Path('.nojekyll').touch()
print('Published files copied to repository root with project-relative URLs.')
