#!/usr/bin/env python3
"""PreToolUse: index.html 편집이 검색엔진 소유확인 태그를 지우려 하면 차단."""
import json, re, sys

TAG = re.compile(r'<meta name="(naver|google)-site-verification" content="[^"]+"\s*/?>')

data = json.load(sys.stdin)
inp = data.get("tool_input", {})
if not str(inp.get("file_path", "")).endswith("index.html"):
    sys.exit(0)

edits = inp.get("edits") or [inp]
for e in edits:
    old = e.get("old_string", "")
    new = e.get("new_string", e.get("content", ""))
    if data.get("tool_name") == "Write":
        try:
            old = open(inp["file_path"], encoding="utf-8").read()
        except OSError:
            old = ""
    lost = {m.group(0) for m in TAG.finditer(old)} - {m.group(0) for m in TAG.finditer(new)}
    if lost:
        print("차단: 네이버/구글 소유확인 meta 태그를 삭제·수정하려 합니다. 이 태그는 유지해야 합니다:\n" + "\n".join(lost), file=sys.stderr)
        sys.exit(2)
sys.exit(0)
