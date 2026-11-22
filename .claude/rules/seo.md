---
paths:
  - "aip-spaces/index.html"
  - "aip-spaces/sitemap.xml"
  - "aip-spaces/robots.txt"
---
# SEO 규칙
- 소유확인 meta(naver ×2, google ×1)는 훅이 보호함. 우회 시도 금지.
- `<title>`, `description`, `og:*`는 같은 메시지를 유지(브랜드명 "에이아이피스페이스 AIP Spaces" 포함).
- JSON-LD `@graph`의 Organization/TravelAgency 정보는 aipproperty.co.kr·aiptravel.kr과 동기화 대상. 값 변경 시 다른 두 사이트도 맞춰야 한다고 알릴 것.
- 화면 FAQ ↔ FAQPage JSON-LD 질문·답변 문구는 1:1 동일.
- canonical·og:url은 `https://www.aipspaces.kr/`(www 포함, 끝 슬래시).
- 실질 콘텐츠 변경 시 sitemap `<lastmod>` 갱신.
