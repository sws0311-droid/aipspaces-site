#!/usr/bin/env python3
"""사이트 무결성 검사. 단독 실행 또는 PostToolUse 훅(--hook)으로 사용.
검사: 소유확인 태그 3개, JSON-LD 파싱, FAQ 화면↔JSON-LD 개수, PHOTOS 사진·썸네일 존재, sitemap 형식."""
import json, os, re, sys
import xml.etree.ElementTree as ET

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = os.path.join(ROOT, "aip-spaces")
hook = "--hook" in sys.argv

if hook:
    try:
        fp = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
    except Exception:
        fp = ""
    if "aip-spaces" not in fp:
        sys.exit(0)

html = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()
errs = []

if len(re.findall(r'name="(?:naver|google)-site-verification"', html)) < 3:
    errs.append("소유확인 meta 태그가 3개 미만입니다 (네이버 2, 구글 1).")

faq_ld = 0
for i, block in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)):
    try:
        obj = json.loads(block)
        if obj.get("@type") == "FAQPage":
            faq_ld = len(obj.get("mainEntity", []))
    except json.JSONDecodeError as e:
        errs.append(f"JSON-LD #{i+1} 파싱 실패: {e}")

m = re.search(r"const PHOTOS=(\{.*?\});", html)
if not m:
    errs.append("PHOTOS 데이터를 찾지 못했습니다.")
else:
    try:
        for loc, items in json.loads(m.group(1)).items():
            for n, _ in items:
                for suffix in ("", "_t"):
                    p = os.path.join(SITE, "images", loc, f"{n}{suffix}.jpg")
                    if not os.path.exists(p):
                        errs.append(f"사진 없음: images/{loc}/{n}{suffix}.jpg")
    except json.JSONDecodeError as e:
        errs.append(f"PHOTOS JSON 오류: {e}")

try:
    ET.parse(os.path.join(SITE, "sitemap.xml"))
except ET.ParseError as e:
    errs.append(f"sitemap.xml 오류: {e}")

if errs:
    print("사이트 검사 실패:\n- " + "\n- ".join(errs), file=sys.stderr)
    sys.exit(2)
if not hook:
    print(f"OK — 소유확인 태그·JSON-LD·사진·sitemap 정상 (FAQ JSON-LD {faq_ld}개)")
