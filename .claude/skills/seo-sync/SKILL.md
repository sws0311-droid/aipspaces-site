---
name: seo-sync
description: FAQ·회사정보·지점 정보를 바꾼 뒤 화면 내용과 JSON-LD·meta·sitemap을 맞추는 작업. "FAQ 추가", "전화번호 바뀌었어", "SEO 정리" 요청 시 사용.
---
# SEO 동기화

1. 변경된 값이 어디에 중복되는지 전부 찾는다: 화면 HTML, `CONFIG`, JSON-LD `@graph`, FAQPage, meta description/og, 푸터.
2. 모든 위치를 같은 값으로 수정. FAQ는 화면 문구와 JSON-LD `acceptedAnswer.text`를 글자 그대로 일치.
3. 회사 정보(사업자번호·주소·대표·연락처·sameAs)가 바뀌었으면: 이 저장소만으론 끝나지 않음 → aipproperty.co.kr, aiptravel.kr에도 같은 수정이 필요하다고 사용자에게 명시.
4. sitemap `<lastmod>` 오늘 날짜.
5. `python3 .claude/hooks/check_site.py` 통과 확인, `seo-auditor` 에이전트로 최종 검토 가능.
