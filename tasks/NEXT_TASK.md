# Current Sprint

**Sprint 2 — 계획 승인 대기.** 계획: [docs/sprints/Sprint-02-UI-Mock-Game-Plan.md](../docs/sprints/Sprint-02-UI-Mock-Game-Plan.md)

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
- [x] Sprint 2 계획 수립 — 계획서 + UI/아트/mock 설계 문서 3종 작성 (2026-08-03, 승인 대기)

---

## Current Blocker

- **Sprint 2 계획 승인 대기.** 승인 전에는 구현을 시작하지 않는다.

## Decision Needed

- Sprint 2 계획 전체 승인 (계획서 §11 승인 필요 항목 포함):
  1. mock 단계 정답 클라이언트 보관 임시 예외
  2. 신규 폴더 `src/lib/data/`·`src/lib/mock/` (+ 문서 폴더 docs/design·docs/architecture)
  3. "별빛 탐험대" 세계관·캐릭터 안
  4. 패키지 후보(설치는 각 Step에서 개별 승인): zustand·react-hook-form·zod·clsx
  5. 한글 웹폰트 (Step 1에서 후보 제시)

## Done Decisions

- Supabase 연결 이연 (2026-08-03): UI·기본 게임 흐름(mock) 구현 이후. 원칙은 docs/00_PROJECT_WORKFLOW.md 데이터 계층 방침·Sprint-01 계획 §12.
- 작업 위치: 로컬 `C:\Users\user\Documents\WM 게임 프로젝트\4. 게임, 퀴즈 프로젝트\01. 방탈출\classquest-builder` (2026-08-02)

## Risk

- 계획서 §12 위험 표 참조 (아트 지연 → P1 우선+placeholder, 범위 팽창 → 배치 편집기는 Sprint 3 이후 등)
