---
name: site-check
description: 배포 전 AIP Spaces 사이트 점검 — 무결성 스크립트, 모바일/데스크톱 스크린샷, 콘솔 오류, 링크·폼 확인. "배포 전 점검", "사이트 확인해줘", "깨진 데 없어?" 같은 요청에 사용.
---
# 사이트 점검

1. `python3 .claude/hooks/check_site.py` 실행 — 실패 항목이 있으면 먼저 고친다.
2. `cd aip-spaces && python3 -m http.server 8080` 을 백그라운드로 띄운다.
3. Playwright(설치되어 있음, `require('playwright')`)로 확인:
   - 뷰포트 390×844, 1440×900 각각 홈·LOCATIONS·각 지점 상세·RESERVATION·FAQ 뷰 스크린샷
   - `console` error, 404 요청 수집
   - `document.documentElement.scrollWidth > innerWidth` 이면 가로 스크롤 문제로 보고
   - 예약 폼: 지점/공간 선택 → 예상 대관료 계산값이 `LOCS` 시간당 요금 × 시간과 일치하는지
   - **폼은 실제로 제출하지 않는다** (FormSubmit이 실제 메일을 보냄).
4. 결과를 표로 보고: 항목 / 통과·실패 / 증거(스크린샷 경로·오류 메시지).
5. 서버 프로세스 종료.
