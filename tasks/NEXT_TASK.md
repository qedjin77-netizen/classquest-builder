# Current Sprint

Sprint 1

## Goal

프로젝트 개발 환경 구축

---

## TODO

- [x] Next.js(App Router) 생성 — 16.2.12, Turbopack, `src/`·`@/*` (2026-08-02, Step 1)
- [x] Tailwind CSS 설정 — v4.3.3, CSS 기반 설정 (2026-08-02, Step 1~2)
- [x] ESLint 설정 — eslint-config-next + eslint-config-prettier (2026-08-02, Step 2)
- [x] Prettier 설정 — prettier-plugin-tailwindcss 포함, format/format:check 스크립트 (2026-08-02, Step 2)
- [x] Husky 설정 — 9.1.7, prepare 스크립트 + pre-commit 훅 (2026-08-02, Step 3)
- [x] lint-staged 설정 — 17.3.0, JS/TS는 ESLint+Prettier, CSS/JSON은 Prettier. 통과·차단 실시험 완료 (2026-08-02, Step 3)
- [ ] 규칙 상수 `src/lib/constants/rules.ts` 생성 (Step 6) ← **다음 작업**
- [ ] Vitest 설정 (Step 7)
- [ ] Playwright 설정 (Step 7)
- [ ] ~~Supabase 연결 준비~~ — **이연** (2026-08-03 결정: UI·기본 게임 흐름 구현 이후. 계획서 §12)
- [x] 환경 변수(.env.example) 생성 — 변수 이름만, 값 없음. `.env.local`은 Supabase 연결 시점(이연)에 작성 (2026-08-02, Step 2)

---

## DONE

- [x] PROJECT.md 작성
- [x] README 작성
- [x] 요구사항 확정 (Sprint 0)
- [x] 워크플로우 문서 작성 (docs/00_PROJECT_WORKFLOW.md)
- [x] Sprint 1 계획 작성 (docs/sprints/Sprint-01-Setup-Plan.md) — 2026-08-02 계획·의존성 A-1~A-7 승인 완료


---

## Current Blocker

- 없음. Step 0~4 완료 (폴더 골격 20개 + 용도 README 생성, 2026-08-03). **다음은 Step 6(규칙 상수 rules.ts)이다.** Step 5(Supabase 연결)는 이연됨 — 계획서 §12.

## Decision Needed

- 없음.

## Done Decisions

- `docs/sprints/Sprint-01-Setup-Plan.md` 승인 (2026-08-02)
- 추가 개발 의존성 A-1~A-7 승인 (2026-08-02)
- **작업 위치를 로컬로 이전 (2026-08-02):** `C:\Users\user\Documents\WM 게임 프로젝트\4. 게임, 퀴즈 프로젝트\01. 방탈출\classquest-builder` — GitHub에서 clone. 새 경로에서 npm 정상 동작 확인(한글 경로 문제 없음).
- **Supabase 연결 이연 (2026-08-03):** 클라우드 프로젝트 생성·키 발급·패키지 설치·연결 코드를 UI와 기본 게임 흐름 구현 이후로 미룬다. UI는 mock data로 먼저 만들고, 데이터 접근 계층은 교체 가능하게 분리한다. 교사 로그인·실시간 참여·데이터 저장 구현 직전에 연결하고, 정식 운영 전 RLS·권한 분리·개인정보·백업·요금제를 검토한다. (docs/00_PROJECT_WORKFLOW.md·계획서 §12에 기록)

## Risk

- Z:에 남은 옛 사본과의 이중 관리 — 개발은 로컬 사본에서만 하고, 동기화는 git(GitHub origin) 경유로만 한다. Z: 사본은 삭제 권장.
- Next.js·Tailwind·Supabase 패키지의 최신 버전과 문서가 계획 작성 시점 이후 달라질 수 있으므로 설치 직전 실제 버전을 확인한다.
