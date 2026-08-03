# Sprint 02 Change Log

## Sprint 정보

- 목표: UI·UX 확정 + mock data 기반 기본 게임 흐름 구현
- 상태: **계획 승인 대기** (2026-08-03 계획 수립)
- 계획: [../docs/sprints/Sprint-02-UI-Mock-Game-Plan.md](../docs/sprints/Sprint-02-UI-Mock-Game-Plan.md)

## Added

- 2026-08-03 — Sprint 2 계획 문서 작성 (`docs/sprint-2-planning` 브랜치, 코드·이미지·패키지 변경 없음):
  - docs/sprints/Sprint-02-UI-Mock-Game-Plan.md — 목표·범위·사용자 흐름·화면 10개·route·컴포넌트·mock 구조·Step 12개·승인 필요 항목·위험·완료 기준
  - docs/design/UI-UX-Guidelines.md — 귀여운 판타지 동화책 방향, 디자인 토큰 계획, 반응형 3구간, 접근성 기준, 저작권 원칙
  - docs/design/Art-Asset-Plan.md — 아트 자산 34종 목록 (파일명 kebab-case, 우선순위 P1~P3, 이미지 미생성)
  - docs/architecture/Mock-Data-Architecture.md — 데이터 접근 계층 분리, mock 정답 임시 예외(승인 대상), Supabase 교체 경로

## Changed

- tasks/NEXT_TASK.md — Sprint 2 계획 승인 대기 상태로 전환
- changelog/README.md — 현재 Sprint를 Sprint 2(계획 승인 대기)로 갱신
- docs/00_PROJECT_WORKFLOW.md — 문서 충돌 우선순위의 세부 설계 문서에 docs/design·docs/architecture 명시

## Decisions

- 계획 승인 전 결정 없음. 승인 필요 항목은 계획서 §11 참조 (mock 정답 임시 예외, 신규 폴더, 세계관·캐릭터 안, 패키지 후보, 웹폰트).

## Verification

- 2026-08-03 — 계획 수립 검증: 문서 변경만 존재(코드·이미지·패키지 없음), 규칙 수치가 rules.ts와 일치(방 3, 문제 3~5, 오답 2→힌트 1, 팀 2~6, 최대 30명), `npm run format:check`·`npm run lint`·`npx tsc --noEmit`·`npm run test` 통과 (결과는 커밋 기록 참조).
