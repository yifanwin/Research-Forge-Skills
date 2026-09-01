#!/usr/bin/env bash
set -euo pipefail
DRY=0; TARGET=""
while [[ $# -gt 0 ]]; do case "$1" in --dry-run) DRY=1; shift;; --target) TARGET=$2; shift 2;; codex) TARGET=${TARGET:-"$HOME/.codex/skills"}; shift;; claude) TARGET=${TARGET:-"$HOME/.claude/skills"}; shift;; kilo) TARGET=${TARGET:-"$HOME/.kilo/skills"}; shift;; *) echo "用法: $0 [--dry-run] [--target DIR|codex|claude|kilo]" >&2; exit 2;; esac; done
[[ -n "$TARGET" ]] || { echo '请指定目标宿主或 --target DIR' >&2; exit 2; }
ROOT=$(cd "$(dirname "$0")/.." && pwd); mkdir -p "$TARGET"
for d in "$ROOT"/skills/*; do [[ -d "$d" ]] || continue; dest="$TARGET/$(basename "$d")"; if [[ $DRY == 1 ]]; then echo "ln -s $d $dest"; elif [[ -e "$dest" || -L "$dest" ]]; then echo "跳过已存在: $dest"; else ln -s "$d" "$dest"; fi; done
