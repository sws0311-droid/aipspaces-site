---
name: add-photos
description: 지점 사진 추가·교체 워크플로 — 리사이즈, 썸네일 생성, PHOTOS 등록, 대표 사진 변경. 사용자가 사진을 올리며 "센트로폴리스에 넣어줘" 같은 요청을 할 때 사용.
---
# 사진 추가

입력: 이미지 파일, 대상 지점id(centropolis | switch22 | lounge107 | signature), 공간명 캡션.

1. 해당 폴더의 마지막 번호 다음부터 두 자리로 번호 부여.
2. Pillow로 변환 (없으면 `pip install pillow`):
   - 원본: 긴 변 1600px, JPEG q=80, EXIF 회전 적용 후 메타데이터 제거
   - 썸네일 `_t`: 긴 변 400px, q=75
3. `index.html`의 `PHOTOS["<지점>"]`에 `["NN", "공간명 · English"]` 추가. "대표로" 요청이면 배열 맨 앞으로.
4. `python3 .claude/hooks/check_site.py` 로 파일 존재 확인.
5. sitemap `<lastmod>` 갱신, 한국어 커밋 메시지 제안.
