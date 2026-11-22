# AIP Spaces 사이트 (www.aipspaces.kr)

에이아이피프라퍼티(AIP Property)의 공간 대관 브랜드 **에이아이피스페이스(AIP Spaces)** 정적 사이트.
서울 도심 4개 지점(센트로폴리스·SWITCH 22·LOUNGE 107·GRAPE LOUNGE) 회의실·세미나·라운지 대관 안내 및 신청.

## 구조
- `aip-spaces/index.html` — 사이트 전체(단일 파일 SPA). CSS·JS·데이터 모두 인라인. 빌드 단계 없음.
  - `CONFIG` — 연락처·운영시간·폼 전송 주소(FormSubmit)·사업자 정보
  - `PHOTOS` — 지점별 사진 `[파일번호, 캡션]`, 첫 항목이 대표 사진
  - `LOCS` — 지점·공간·요금 `[공간명, 면적(평), 수용, 1인당, 시간당, 비고]`, `null` = 별도 문의
  - `SVCS`, `FLOW` — 서비스 카드, 대관 절차
  - 뷰 전환: `<div class="view" id="v-...">` + `data-go` 속성
- `aip-spaces/images/<지점id>/NN.jpg`(원본) + `NN_t.jpg`(썸네일) — 항상 쌍으로 존재
- `aip-spaces/sitemap.xml`, `robots.txt`

## 명령
- 로컬 미리보기: `cd aip-spaces && python3 -m http.server 8080`
- 사이트 무결성 검사: `python3 .claude/hooks/check_site.py`

## 절대 규칙
- `<head>`의 네이버·구글 소유확인 meta 태그는 **삭제·수정 금지**.
- JSON-LD(Organization/FAQPage)의 회사 정보는 aipproperty.co.kr·aiptravel.kr과 일치해야 함 → 바꾸면 3개 사이트 모두 맞춰야 한다고 사용자에게 알릴 것.
- 화면 FAQ를 바꾸면 FAQPage JSON-LD도 같이 수정.
- 콘텐츠를 실질적으로 바꾸면 `sitemap.xml`의 `<lastmod>`를 오늘 날짜로.
- 카카오톡 채널은 현재 비활성(`kakaoUrl: ''`) — 요청 없이 다시 켜지 말 것.
- 사용자 대면 문구는 한국어, 존댓말(-습니다/-요).
- 커밋 메시지는 한국어, 변경 요지를 한 줄로 (기존 로그 스타일).

## 세부 규칙
`.claude/rules/` 참고 — html-css, seo, images, copy-ko.
