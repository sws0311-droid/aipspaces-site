---
paths:
  - "aip-spaces/**/*.html"
---
# HTML·CSS·JS 규칙
- 단일 파일 유지: 새 CSS/JS 파일을 만들지 말고 `index.html` 안에 인라인으로.
- 색은 `:root` 토큰(`--ink`, `--navy`, `--gold`, `--cream`, `--paper` …)만 사용. 새 hex 하드코딩 금지.
- 폰트: 본문 Noto Sans KR, 제목 Noto Serif KR, 영문 장식 Cormorant Garamond(`.en`). 다른 웹폰트 추가 금지.
- 지점·요금·사진은 HTML에 직접 쓰지 말고 `LOCS`/`PHOTOS`/`SVCS` 데이터만 수정 → 렌더 함수가 그림.
- 모바일 우선 확인: 360px 폭에서 가로 스크롤 없을 것. 표는 `.tbl-wrap` 안에.
- 폼은 `CONFIG.formEndpoint`(FormSubmit)로 전송, 실패 시 `fallbackModal` 메일 링크. 이 흐름을 깨지 말 것.
- 외부 스크립트(분석·채팅 위젯 등) 추가는 사용자 확인 후에만.
