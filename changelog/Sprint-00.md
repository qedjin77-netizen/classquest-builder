# Sprint 00 Change Log

## 2026-08-02

### Added

- PROJECT.md — 프로젝트 전체 사양
- CLAUDE.md — Claude Code 개발 규칙
- README.md — 프로젝트 소개
- docs/01_REQUIREMENTS_DECISIONS.md — 요구사항 확정 (Sprint 0, D-01 ~ D-12)
- docs/00_PROJECT_WORKFLOW.md — 개발 워크플로우 (역할 · 작업 순서 · 승인 규칙)
- docs/archive/02_SPRINT_00_PLAN_REPLACED.md — (구) Sprint 0 셋업 계획 — 미승인, 03으로 대체됨
- docs/sprints/Sprint-01-Setup-Plan.md — Sprint 1 셋업 계획 (승인 대기)
- tasks/NEXT_TASK.md — 현재 Sprint 목표와 TODO/DONE
- changelog/Sprint-00.md — 이 문서

### Decisions

- Sprint 번호 체계 확정: Sprint 0은 요구사항 확정, Sprint 1은 프로젝트 셋업이다.
- 문서 충돌 시 `PROJECT.md` → `01_REQUIREMENTS_DECISIONS.md` → `CLAUDE.md` → 승인된 Sprint 계획 → `README.md` 순으로 판단한다.
- `docs/02_ARCHITECTURE.md`를 구현 구조의 기준 문서로 추가한다.

### Changed

- CLAUDE.md — 상단 중복 체크리스트를 간결한 개발 워크플로우로 교체, 필독 목록에 tasks/NEXT_TASK.md 반영
- docs 파일 번호 재정렬 — 00_PROJECT_WORKFLOW → 01_REQUIREMENTS_DECISIONS → 02_SPRINT_00_PLAN(구) → 03_SPRINT_01_SETUP_PLAN 순. 참조 링크 전체 갱신
- README.md — 문서 구조 트리에 tasks/NEXT_TASK.md · changelog/Sprint-00.md · docs 4개 파일 반영, 읽는 순서에 워크플로우 문서 추가
- docs/archive/02_SPRINT_00_PLAN_REPLACED.md — 문서 상단에 "대체됨" 표시 추가
- docs/00_PROJECT_WORKFLOW.md — Lead Developer 역할에 Sprint 계획 초안 작성 명시 (역할 정의와 실제 작성 주체 일치)
- tasks/NEXT_TASK.md — TODO에 lint-staged 추가, DONE에 워크플로우 문서 · Sprint 1 계획 작성 반영

---

다음 예정

Sprint 1 — 프로젝트 개발 환경 구축 (계획 승인 대기)


## 문서 구조 마이그레이션

초기 루트 문서 구조를 Sprint·작업·결정 기록 중심 구조로 재편했다.

- 구 `NEXT_TASK.md` → `tasks/NEXT_TASK.md`
- 구 루트 `CHANGELOG.md` → `changelog/Sprint-00.md`
- 구 Sprint 0 계획 문서 → `docs/archive/02_SPRINT_00_PLAN_REPLACED.md`
- 현재 Sprint 계획 → `docs/sprints/Sprint-01-Setup-Plan.md`

이 항목은 파일의 과거 이름과 현재 위치를 함께 기록하기 위한 것이다.
