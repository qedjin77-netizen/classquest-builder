# Done

완료된 주요 작업을 Sprint 단위로 요약한다. 상세 변경 내용은 `changelog/`를 본다.

## Sprint 00 — 요구사항 확정

- [x] 프로젝트 범위와 대상 확정
- [x] 게임 진행 규칙 확정
- [x] 개인전·팀전 규칙 확정
- [x] 보안·버전·자산 정책 확정
- [x] 프로젝트 운영 문서 작성
- [x] Sprint 1 프로젝트 셋업 계획 작성

## Sprint 01 — 프로젝트 셋업 (2026-08-03 완료)

- [x] Z: 드라이브 검증 → 로컬 C: 이전으로 개발 환경 확보 (Step 0)
- [x] Next.js 16.2.12 스캐폴딩 — TypeScript strict, Tailwind v4, App Router, `src/`·`@/*` (Step 1)
- [x] 설정 고정 — `.gitattributes`, `.gitignore`, `.env.example`(이름만), Prettier + eslint-config-prettier (Step 2)
- [x] Husky + lint-staged pre-commit — 통과·차단 실시험 완료 (Step 3)
- [x] 폴더 골격 20개 + 용도 README (Step 4)
- [x] 규칙 상수 `src/lib/constants/rules.ts` 8개 (Step 6)
- [x] Vitest 4/4·Playwright(Chromium) 1/1 예시 테스트 통과 (Step 7)
- [x] 최종 검증·README 정리·PR 생성 (Step 8)
- 이연: Step 5 Supabase 연결 — UI·기본 게임 흐름(mock data) 구현 이후 (2026-08-03 결정, 계획서 §12)
