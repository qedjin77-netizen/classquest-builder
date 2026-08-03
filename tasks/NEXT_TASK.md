# Current Sprint

**Sprint 2 — 계획 교정 완료 · 최종 승인 대기.** 계획: [docs/sprints/Sprint-02-UI-Mock-Game-Plan.md](../docs/sprints/Sprint-02-UI-Mock-Game-Plan.md)
다음 작업: **Sprint 2 계획 최종 승인 후 Step 1 진행** (승인 전 구현 시작 금지)

## Goal

UI·UX 확정 + mock data 기반 기본 게임 흐름 구현 (Supabase 없이)

---

## TODO (계획 승인 후 Step 순서대로, Step마다 승인 게이트)

- [ ] Step 1 — UI·아트 가이드와 디자인 토큰 확정
- [ ] Step 2 — 전체 화면 구조·사용자 흐름 확정
- [ ] Step 3 — 공통 레이아웃·기본 컴포넌트
- [ ] Step 4 — 시작 화면
- [ ] Step 5 — 교사용 제작기 기본 화면
- [ ] Step 6 — 문제 입력·방 구성 흐름
- [ ] Step 7 — 학생 참여·대기실 mock 화면
- [ ] Step 8 — 학생용 방 탈출 기본 화면
- [ ] Step 9 — 문제 풀이·힌트·진행 상태 mock 로직
- [ ] Step 10 — 결과 화면
- [ ] Step 11 — 반응형·접근성·테스트 보완
- [ ] Step 12 — Sprint 2 전체 검증·PR

---

## DONE

- [x] Sprint 1 — 프로젝트 셋업 완료 (2026-08-03, PR #1 main 병합. 요약: [DONE.md](DONE.md))
- [x] Sprint 2 계획 수립 — 계획서 + UI/아트/mock 설계 문서 3종 작성 (2026-08-03)
- [x] Sprint 2 계획 검토 오류 교정 — 자산 우선순위 수량(P1 14·P2 14·P3 6), Step 4 자산 모순 해소, 자산 제작 시점 Step별 명확화, 승인/미승인 항목 정리 (2026-08-03)

---

## Current Blocker

- **Sprint 2 계획 최종 승인 대기.** 승인 전에는 Step 1을 포함해 구현을 시작하지 않는다.

## Decision Needed

- **Sprint 2 계획 최종 승인** (교정 반영본). 개별 항목 중 다음은 아직 미승인 상태로 유지: zustand·react-hook-form·zod·clsx 설치(필요 확인 Step에서 개별 승인), 한글 웹폰트 확정·설치(Step 1에서 후보·라이선스·성능 보고 후 승인).

## Done Decisions

- **Sprint 2 선승인 항목 (2026-08-03):** ① mock 단계 한정 정답·판정의 클라이언트 데이터 계층 보관(임시 예외) ② 신규 폴더 `src/lib/data/`·`src/lib/mock/`·`docs/design/`·`docs/architecture/` ③ "별빛 탐험대" 세계관과 학생 모험가·별 요정 안내 캐릭터 방향 ④ 기본 상태 관리 = React state + Context ⑤ 기본 폼 검증 = 직접 구현. (계획서 §11.1)
- Supabase 연결 이연 (2026-08-03): UI·기본 게임 흐름(mock) 구현 이후. 원칙은 docs/00_PROJECT_WORKFLOW.md 데이터 계층 방침·Sprint-01 계획 §12.
- 작업 위치: 로컬 `C:\Users\user\Documents\WM 게임 프로젝트\4. 게임, 퀴즈 프로젝트\01. 방탈출\classquest-builder` (2026-08-02)

## Risk

- 계획서 §12 위험 표 참조 (아트 지연 → P1 우선+placeholder, 범위 팽창 → 배치 편집기는 Sprint 3 이후 등)
