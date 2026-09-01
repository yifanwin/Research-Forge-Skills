#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "用法: $0 PROJECT_DIR" >&2
  exit 2
}

[[ $# -eq 1 ]] || usage
PROJECT=$(cd "$1" 2>/dev/null && pwd || true)
if [[ -z "$PROJECT" ]]; then
  mkdir -p "$1"
  PROJECT=$(cd "$1" && pwd)
fi

ROOT=$(cd "$(dirname "$0")/.." && pwd)

if [[ -e "$PROJECT/AGENTS.md" || -e "$PROJECT/.research" ]]; then
  echo "目标项目已存在 AGENTS.md 或 .research，拒绝覆盖: $PROJECT" >&2
  exit 1
fi

mkdir -p "$PROJECT/.research"/{proposal,project,archive,reports,knowledge/{papers,reviews,pdfs}}
cp "$ROOT/templates/AGENTS.md" "$PROJECT/AGENTS.md"
cp "$ROOT/templates/research-root/global.md" "$PROJECT/.research/global.md"
cp "$ROOT/templates/research-root/TODO.md" "$PROJECT/.research/TODO.md"

echo "项目骨架已创建: $PROJECT"
echo "请编辑 $PROJECT/AGENTS.md，填写研究目标、成功判据和工具链。"
