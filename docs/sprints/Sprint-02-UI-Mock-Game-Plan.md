# Sprint 2 — UI·Mock 게임 흐름 계획

| 항목 | 내용 |
| --- | --- |
| 스프린트 | Sprint 2 (UI·UX 확정 + mock data 기반 기본 게임 흐름) |
| 작성일 | 2026-08-03 |
| 상태 | **승인 대기** |
| 선행 문서 | [PROJECT.md](../../PROJECT.md) · [CLAUDE.md](../../CLAUDE.md) · [../00_PROJECT_WORKFLOW.md](../00_PROJECT_WORKFLOW.md) · [../01_REQUIREMENTS_DECISIONS.md](../01_REQUIREMENTS_DECISIONS.md) |
| 세부 설계 | [../design/UI-UX-Guidelines.md](../design/UI-UX-Guidelines.md) · [../design/Art-Asset-Plan.md](../design/Art-Asset-Plan.md) · [../architecture/Mock-Data-Architecture.md](../architecture/Mock-Data-Architecture.md) |

> 이 문서는 계획이다. **승인 전에는 코드·CSS·mock data·이미지를 만들지 않고, 패키지를 설치하지 않는다.**
> 승인 후에도 각 Step은 사용자 승인 없이 다음 Step으로 자동 진행하지 않는다.

---

## 1. 목표

- 서비스 전체 UI·UX 방향과 독창적 아트 스타일(귀여운 판타지 동화책)을 확정한다.
- 교사용 게임 제작기와 학생용 방탈출 플레이의 **기본 흐름을 mock data로 끝까지 동작**하게 만든다.
- 데이터 접근 계층을 분리해 이후 Supabase 교체가 쉬운 구조를 만든다.

## 2. 범위

- 시작 화면, 교사용 제작 흐름(새 게임→기본 정보→방 3개→문제 3~5개/방→정답·해설·힌트→미리보기→임시 저장→시작 준비), 학생용 플레이 흐름(참여→대기실→방 1~3 탐색·풀이→결과)
- 공통 UI 컴포넌트·디자인 토큰, 반응형·접근성 기본, 아트 자산 목록 기반 이미지 제작(각 Step 승인 후)
- Vitest·Playwright 테스트 보강

## 3. 범위 제외

- Supabase 일체(프로젝트·키·패키지·연결·DB 스키마) — [Sprint-01 계획 §12](Sprint-01-Setup-Plan.md#12-일정-변경--supabase-연결-이연-2026-08-03) 이연 유지
- 교사 로그인·회원, 실제 참여 코드 통신, 실시간 학생 목록, 영구 저장(게시·불변 버전 스냅샷)
- **자유 드래그 배치 편집기**(이동·크기·회전·복사·잠금·레이어·Undo/Redo) — Sprint 3 이후. Sprint 2의 "방 구성"은 배경 선택+문제 목록 관리 수준
- 팀전, 오디오, 콘텐츠 공유, 도움 요청/교사 확인, 재접속 복구, CI/배포

## 4. 전제 조건

- Sprint 1 완료 상태(main `048be2e`) 기준. 기존 폴더 구조·파일명·`rules.ts` 상수 8개를 변경하지 않는다.
- 게임 규칙 수치는 항상 `src/lib/constants/rules.ts`를 import해서 쓴다 (방 3, 문제 3~5, 오답 2회→힌트 1개, 팀 2~6, 최대 30명).

## 5. 사용자 흐름

### A. 교사용 (mock)

시작 화면 → 교사용 메뉴 → 새 게임 만들기 → 제목·기본 정보 입력 → 방 3개 구성(배경 선택) → 방마다 문제 3~5개 입력 → 문제별 정답·해설·힌트 입력 → 게임 미리보기(학생 화면 재사용) → 임시 저장(localStorage) → 게임 시작 준비 화면

### B. 학생용 (mock)

시작 화면 → 참여 코드+닉네임 입력(형식 검증만) → 대기실 → 게임 시작 → 방 탐색(오브젝트 클릭) → 문제 확인 → 정답 제출 → 오답 2회 후 힌트 1개 해제 → 방별 전 문제 해결 시 출구 개방 → 방 3개 탈출 → 결과 화면(소요 시간·정답 수)

## 6. 화면·route 목록 (App Router, 기존 라우트 그룹 사용)

| # | 화면 | route | 파일 위치 |
| --- | --- | --- | --- |
| S1 | 시작 화면 | `/` | `src/app/page.tsx` (스캐폴드 페이지 교체) |
| S2 | 교사용 메뉴 | `/teacher` | `src/app/(teacher)/teacher/page.tsx` |
| S3 | 새 게임(기본 정보) | `/teacher/games/new` | `src/app/(teacher)/teacher/games/new/page.tsx` |
| S4 | 게임 편집(방·문제) | `/teacher/games/[gameId]/edit` | `src/app/(teacher)/teacher/games/[gameId]/edit/page.tsx` |
| S5 | 미리보기 | `/teacher/games/[gameId]/preview` | `src/app/(teacher)/teacher/games/[gameId]/preview/page.tsx` |
| S6 | 시작 준비 | `/teacher/games/[gameId]/ready` | `src/app/(teacher)/teacher/games/[gameId]/ready/page.tsx` |
| S7 | 학생 참여 | `/play` | `src/app/(play)/play/page.tsx` |
| S8 | 대기실 | `/play/waiting` | `src/app/(play)/play/waiting/page.tsx` |
| S9 | 방 화면 | `/play/room/[roomNo]` | `src/app/(play)/play/room/[roomNo]/page.tsx` (roomNo 1~3) |
| S10 | 결과 화면 | `/play/result` | `src/app/(play)/play/result/page.tsx` |

- 공통 layout: 루트 `layout.tsx`(토큰·폰트) + `(teacher)/layout.tsx`(관리 화면 헤더) + `(play)/layout.tsx`(게임 화면 프레임)
- 미리보기(S5)는 학생 방 화면 컴포넌트를 재사용한다 (별도 판정 경로 금지 원칙의 UI 버전)

## 7. 컴포넌트 계획 (`src/components/ui/` + `src/features/*`)

- 공통(ui): `AppButton` `AppInput` `AppTextarea` `AppSelect` `Card` `Modal` `Badge` `ProgressSteps`(방 진행) `StatusIcon`(정답·오답·힌트·완료) `GuideBubble`(안내 캐릭터+말풍선) `EmptyState` `LoadingState` `ErrorMessage`
- builder(features): `GameInfoForm` `RoomTabs` `QuestionList` `QuestionForm`(유형별 입력: 객관식·복수정답·단답·OX) `PublishChecklist`(mock 검증 표시)
- play(features): `RoomScene`(배경+오브젝트) `QuestionModal` `HintBox` `AnswerFeedback` `ExitDoor` `ResultSummary`
- 폼 검증: 기본은 controlled state + 직접 검증(필수값·글자 수·문제 수 3~5). 라이브러리는 §11 승인 필요 항목

## 8. mock data 구조

[Mock-Data-Architecture.md](../architecture/Mock-Data-Architecture.md) 기준. 요약: `src/lib/data/`(계약+mock 구현)·`src/lib/mock/fixtures.ts`(샘플 게임 1개)·`src/types/`(공용 타입). 판정·힌트 해제 로직은 데이터 계층 안에만 두고 화면은 결과만 받는다. **mock 단계의 정답 클라이언트 보관은 임시 예외로 승인 대상** (§11-1).

## 9. 아트 자산

[Art-Asset-Plan.md](../design/Art-Asset-Plan.md) 기준 — 총 **34종** (학생 캐릭터 2, 안내 캐릭터 2, 방 배경 5, 오브젝트 9, 상태 아이콘 4, 로고·장식 2, 교사 UI 아이콘 7, 버튼·패널 3). P1 12종이 화면 Step의 선행 조건이며, 이미지 생성은 각 Step에서 승인 후 진행한다.

## 10. Step별 작업 계획

> 공통 검증 명령: `npm run lint` · `npx tsc --noEmit` · `npm run format:check` · `npm run test` · `npm run build` (화면 Step은 `npm run test:e2e` 추가). 각 Step 종료 시 결과 보고 후 **사용자 승인을 받고** 다음으로 진행한다.

| Step | 작업 내용 | 주요 산출물 | 변경 예상 파일 | 완료 조건 | 테스트 방법 |
| --- | --- | --- | --- | --- | --- |
| 1 | UI·아트 가이드와 디자인 토큰 확정 (아트 선행) | 확정된 UI-UX-Guidelines·Art-Asset-Plan, `@theme` 토큰 값 표 | docs/design/* (문서 확정), `src/app/globals.css`(토큰만) | 토큰 이름·값 확정, 세계관·캐릭터 안 승인 | format/lint/빌드 통과, 토큰 문서-코드 일치 육안 확인 |
| 2 | 전체 화면 구조·사용자 흐름 확정 | route 트리, 화면별 와이어 설명(문서) | 본 계획서 §6 확정 표기 | 화면 10개·route 확정 | 문서 검토 |
| 3 | 공통 레이아웃·기본 컴포넌트 | 루트/(teacher)/(play) layout, AppButton·AppInput·Card·Modal·StatusIcon 등 | `src/app/*/layout.tsx`, `src/components/ui/*` | 컴포넌트 데모 렌더 확인, 접근성(포커스·44px) 충족 | 단위 렌더 테스트 + lint/tsc |
| 4 | 시작 화면 (P1 로고·배경·캐릭터 제작 선행) | S1 완성 | `src/app/page.tsx`, assets | 시작→교사/학생 분기 이동 동작 | e2e: 시작 화면 렌더·이동 |
| 5 | 교사용 제작기 기본 화면 | S2·S3 (메뉴, 새 게임 폼) | `(teacher)/*`, features/builder 일부, data 계층 골격 | 새 게임 생성→편집 화면 진입(mock) | e2e: 교사 흐름 앞부분 |
| 6 | 문제 입력·방 구성 흐름 | S4 (방 탭+문제 CRUD+검증 3~5개) | features/builder, lib/data, lib/mock | 방 3개·문제 3~5개 입력, 정답·해설·힌트 입력, 임시 저장 | 단위: 폼 검증·저장, e2e: 제작 관통 |
| 7 | 학생 참여·대기실 mock 화면 | S7·S8 | `(play)/*`, features/play 일부 | 코드 형식 검증→대기실→시작 버튼 | e2e: 참여 흐름 |
| 8 | 학생용 방 탈출 기본 화면 (P1 배경·오브젝트 선행) | S9 (방 탐색, 오브젝트 클릭→문제 모달) | features/play, RoomScene | 방 1 탐색·문제 열람 동작 | e2e: 방 진입·모달 |
| 9 | 문제 풀이·힌트·진행 상태 mock 로직 | 판정·오답 2회 힌트·출구 개방·방 이동 | lib/data(판정), features/play | 정답 처리·힌트 해제(개인·문제별 2회)·방 1→2→3 이동 | **단위: 판정·힌트·출구 조건**, e2e: 풀이 |
| 10 | 결과 화면 | S10 (+S5·S6 미리보기·시작 준비 마감) | (play)/result, (teacher)/preview·ready | 3방 탈출→결과(시간·정답 수), 미리보기=학생 화면 재사용 | e2e: 전체 관통(교사 제작→학생 탈출) |
| 11 | 반응형·접근성·테스트 보완 (P2·P3 자산 반영) | 3 구간 반응형, 접근성 점검표 통과 | 전 화면 스타일, 테스트 추가 | 375/768/1280 확인, 색상 단독 구분 없음, 대비 4.5:1 | e2e 뷰포트별, 수동 점검표 |
| 12 | Sprint 2 전체 검증·문서 정리·PR | 최종 검증 기록, PR | docs·tasks·changelog | §13 완료 기준 전부 충족 | 전 명령 + e2e 전체 |

> 순서 검토: 기본안 그대로 채택한다. 근거 — 토큰·가이드(1)가 모든 화면의 선행 조건이고, 판정 로직(9)은 방 화면(8) 없이 검증 화면이 없다. 아트는 각 화면 Step의 선행 조건으로 표기했다(P1 우선).

## 11. 승인 필요 항목

| # | 항목 | 내용 |
| --- | --- | --- |
| 1 | **mock 정답 임시 예외** | mock 단계에서 정답·판정이 클라이언트 데이터 계층에 존재 (CLAUDE.md 3.2·3.3의 최종 기준은 Supabase 연결 시 회복). 상세: Mock-Data-Architecture §3 |
| 2 | **신규 폴더** | `src/lib/data/`, `src/lib/mock/`, (문서) `docs/design/`, `docs/architecture/` — 폴더 구조 변경 승인 |
| 3 | **세계관·캐릭터 안** | "별빛 탐험대" 세계관, 학생 모험가·별 요정 안내 캐릭터 (독창 창작) |
| 4 | 패키지 후보 (지금 설치 안 함) | `zustand`(상태 — 대안: Context, Context로 시작), `react-hook-form`+`zod`(폼 — 대안: 직접 검증, 직접 검증으로 시작), `clsx`(클래스 조합 — 대안: 템플릿 리터럴). **설치 시점: 해당 Step에서 필요가 입증될 때 개별 승인** |
| 5 | 한글 웹폰트 | 무료 라이선스 확인된 귀여운 계열 1종 — Step 1에서 후보 제시 후 승인 |

## 12. 위험 요소와 대응

| 위험 | 대응 |
| --- | --- |
| 아트 제작 지연이 화면 Step을 막음 | P1만 선행 조건으로 하고, 미완 시 회색 도형 placeholder로 진행 후 교체 |
| mock 정답 노출 예외가 습관화됨 | 판정 로직을 데이터 계층에 격리 + Supabase 전환 체크리스트를 §11-1 승인 문구에 고정 |
| 제작기 범위 팽창(자유 배치 욕심) | §3 범위 제외 명시 — 배치 편집은 Sprint 3 이후, 이번엔 목록 기반 |
| Context만으로 상태가 복잡해짐 | 편집/플레이 상태를 분리 설계, 한계 도달 시 근거와 함께 패키지 승인 요청 |
| 화면 다수를 한꺼번에 구현 | Step당 화면 1~2개로 제한, Step 종료마다 승인 게이트 |

## 13. Sprint 2 최종 완료 기준

- 교사가 mock으로 게임 1개(방 3, 문제 9~15)를 만들고 미리보기·임시 저장·시작 준비까지 도달한다.
- 학생이 mock으로 참여→방 1~3 풀이→탈출→결과까지 완주한다. 오답 2회→힌트 1개, 전 문제 해결→출구 개방이 정확히 동작한다.
- 미리보기가 학생 화면 컴포넌트를 재사용한다.
- 판정·힌트·출구 로직에 Vitest 테스트, 교사·학생 관통 흐름에 Playwright 테스트가 있다.
- 반응형 3구간·접근성 기준(색상 단독 구분 금지, 대비, 포커스) 충족.
- lint·tsc·format·test·test:e2e·build 전부 통과. Supabase 코드·패키지 0건 유지.

## 14. Supabase 연결 시점

Sprint 2 완료 후, **교사 로그인·실시간 학생 참여·데이터 저장을 구현하기 직전** Sprint에서 연결한다 (Sprint-01 계획 §12·워크플로우 데이터 계층 방침 유지). 연결 시 mock 구현체를 서버 구현체로 교체하고 C-9(server-only) 검증을 수행한다.

## 15. Sprint 3 이후로 넘기는 항목

Supabase 연결·스키마·RLS, 교사 로그인, 게시·불변 버전, 자유 드래그 배치 편집기, 팀전, 실시간 대시보드, 도움 요청·교사 확인, 재접속 복구, 오디오, 콘텐츠 공유·검색·복제, 부하·배포
