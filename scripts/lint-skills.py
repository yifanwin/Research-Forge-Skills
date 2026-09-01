#!/usr/bin/env python3
import re,sys
try:
 import yaml
except ImportError: yaml=None
from pathlib import Path
root=Path(__file__).resolve().parents[1]; skills=root/'skills'; errors=[]
pat=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
for d in sorted(skills.iterdir()):
 if not d.is_dir(): continue
 f=d/'SKILL.md'
 if not f.exists(): errors.append(f'{d.name}: missing SKILL.md'); continue
 t=f.read_text()
 if not t.startswith('---\n'): errors.append(f'{d.name}: missing frontmatter'); continue
 end=t.find('\n---',4)
 if end<0: errors.append(f'{d.name}: invalid frontmatter'); continue
 fm=t[4:end]
 if yaml:
  try: yaml.safe_load(fm)
  except Exception as e: errors.append(f'{d.name}: invalid YAML frontmatter ({e})')
 m=re.search(r'^name:\s*(\S+)',fm,re.M); desc=re.search(r'^description:\s*(.*)',fm,re.M)
 if not m: errors.append(f'{d.name}: missing name')
 else:
  n=m.group(1)
  if n!=d.name: errors.append(f'{d.name}: name mismatch ({n})')
  if not pat.match(n): errors.append(f'{d.name}: name not kebab-case')
 if not desc or not desc.group(1).strip(): errors.append(f'{d.name}: missing description')
 if re.search(r'^requires:',fm,re.M): errors.append(f'{d.name}: requires is forbidden')
 if '.kilo/' in t or 'my_skills/' in t: errors.append(f'{d.name}: legacy path')
 if len(t.splitlines())>500: errors.append(f'{d.name}: SKILL.md exceeds 500 lines')
 for ref in re.findall(r'`((?:references/)[^`]+)`|\]\((references/[^)]+)\)',t):
  p=next(x for x in ref if x); 
  if not (d/p).exists(): errors.append(f'{d.name}: missing reference {p}')
 if (d/'references').exists() and any(x.is_dir() for x in (d/'references').rglob('*')): errors.append(f'{d.name}: nested references')
if errors:
 print('\n'.join('ERROR '+e for e in errors)); sys.exit(1)
print(f'PASS: {sum(1 for d in skills.iterdir() if d.is_dir())} skills validated')
