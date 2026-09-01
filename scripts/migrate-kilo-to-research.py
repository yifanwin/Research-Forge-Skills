#!/usr/bin/env python3
import argparse, shutil, sys
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('project',type=Path); p.add_argument('--dry-run',action='store_true'); a=p.parse_args()
src=a.project/'.kilo'; dst=a.project/'.research'
if not src.is_dir(): print(f'源目录不存在: {src}',file=sys.stderr); sys.exit(1)
if dst.exists(): print(f'目标已存在，拒绝覆盖: {dst}',file=sys.stderr); sys.exit(1)
files=list(src.rglob('*')); print(f'迁移 {src} -> {dst} ({len(files)} 个条目)')
if a.dry_run: sys.exit(0)
try:
 shutil.copytree(src,dst)
 for f in dst.rglob('*'):
  if f.is_file() and f.suffix.lower() in ('.md','.markdown'):
   s=f.read_text(); f.write_text(s.replace('.kilo/','.research/').replace('.kilo\\','.research\\'))
except Exception as e:
 if dst.exists(): shutil.rmtree(dst)
 print(f'迁移失败: {e}',file=sys.stderr); sys.exit(1)
print('迁移完成；源目录未删除。')
