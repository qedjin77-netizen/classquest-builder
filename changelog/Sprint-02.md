# Sprint 02 Change Log

## Sprint 정보

- 목표: UI·UX 확정 + mock data 기반 기본 게임 흐름 구현
- 상태: **계획 교정 완료 · 최종 승인 대기** (2026-08-03 계획 수립 → 검토 오류 교정). 다음 작업: 최종 승인 후 Step 1
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

## Fixed

- 2026-08-03 — 계획 검토 오류 교정 (구현·이미지·패키지 변경 없음):
  - Art-Asset-Plan 합계 오기 정정: P1 12·P2 13·P3 9 → **P1 14·P2 14·P3 6** (표 실집계 기준. 총 34종·범주별 수량은 변동 없음, 항목 추가·삭제 없음)
  - Step 4 자산 모순 해소: "P1 로고·배경·캐릭터 선행" → 선행 자산을 P1 3종(logo-classquest·student-adventurer·guide-star-fairy)으로 한정. `start-bg.jpg`는 P2 유지, 제작 전 CSS 배경/placeholder 사용 명시
  - 자산 제작 시점 명확화: 일괄 선제작이 아니라 **사용하는 화면의 Step 직전에 필요한 것만** 제작 (Step 4: 3종 / Step 8: 7종 / Step 9: 4종 / P2: 완성도 보완 시 / P3: Step 11 재확인 후). 제작은 승인 후 소규모 세트, placeholder로 코드 검증 가능

## Decisions

- **2026-08-03 승인됨 (계획서 §11.1):** ① mock 단계 한정 정답·판정의 클라이언트 데이터 계층 보관(임시 예외) ② 신규 폴더 src/lib/data·src/lib/mock·docs/design·docs/architecture ③ "별빛 탐험대" 세계관·학생 모험가·별 요정 캐릭터 방향 ④ 기본 상태 관리 React state+Context ⑤ 기본 폼 검증 직접 구현
- **미승인 유지 (계획서 §11.2):** zustand·react-hook-form·zod·clsx 설치(필요 확인 Step에서 개별 승인), 한글 웹폰트(Step 1에서 후보·라이선스·성능 보고 후 승인)

## Verification

- 2026-08-03 — 계획 수립 검증: 문서 변경만 존재(코드·이미지·패키지 없음), 규칙 수치가 rules.ts와 일치(방 3, 문제 3~5, 오답 2→힌트 1, 팀 2~6, 최대 30명), `npm run format:check`·`npm run lint`·`npx tsc --noEmit`·`npm run test` 통과 (결과는 커밋 기록 참조).
