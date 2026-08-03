# Mock Data Architecture — Sprint 2

| 항목 | 내용 |
| --- | --- |
| 상태 | **초안 — Sprint 2 계획 승인 대기** |
| 상위 기준 | [../02_ARCHITECTURE.md](../02_ARCHITECTURE.md) · [../00_PROJECT_WORKFLOW.md](../00_PROJECT_WORKFLOW.md) 데이터 계층 방침 |
| 원칙 | Supabase 연결 이연 — **UI·기본 게임 흐름은 mock data와 로컬 상태로 구현**하고, 데이터 접근 계층을 분리해 나중에 Supabase로 교체하기 쉽게 만든다 |

> 이 문서는 계획이다. 승인 전에는 mock data와 코드를 생성하지 않는다.

---

## 1. 계층 구조

```text
화면 컴포넌트 (src/app/*, src/features/*)
        │  훅·함수 호출만 한다. 데이터 출처를 모른다.
        ▼
데이터 접근 계층 (src/lib/data/)          ← 인터페이스(계약)
├─ game-repository.ts     교사 제작 게임 CRUD 계약
├─ play-session.ts        학생 세션·진행·판정 계약
└─ mock/                  Sprint 2 구현체 (fixtures + 로컬 상태)
        ▼ (Supabase 연결 시점에 구현체만 교체)
향후: src/server/* + src/lib/supabase/ 기반 구현체
```

- 화면은 **인터페이스만 의존**한다. `import ... from "@/lib/data/..."` 외에 데이터 출처를 아는 코드를 화면에 두지 않는다.
- Supabase 전환은 **구현체 파일 교체 + 조립 지점 1곳 수정**으로 끝나는 것을 목표로 한다.
- `src/lib/data/`와 `src/lib/mock/`(fixtures)은 **신규 폴더**다 — 폴더 구조 변경이므로 Sprint 2 계획 승인에 포함해 승인받는다.

## 2. mock data 위치와 구성

| 위치 | 내용 |
| --- | --- |
| `src/lib/mock/fixtures.ts` | 샘플 게임 1개 — 방 3개, 방당 문제 3~5개(총 9~15문제), 각 문제에 정답·힌트 1개·해설 |
| `src/lib/data/mock/*` | mock 구현체 — fixtures 로드, 로컬 상태 관리, 판정 함수 |
| `src/types/` | `Game`·`Room`·`Question`·`StudentSession`·`Progress` 등 공용 타입 |

- 샘플 데이터 규모는 `src/lib/constants/rules.ts` 상수를 **import해서** 준수를 테스트로 강제한다 (값 복붙 금지).
- 학생 진행 상태(닉네임, 현재 방, 문제별 오답 횟수, 힌트 해제)는 메모리 상태 + `localStorage`(새로고침 복구 흉내)로 관리한다.
- 참여 코드는 실제 통신 없이 **형식 검증만** 하는 mock이다 (어떤 코드든 대기실로 진입).

## 3. 판정 로직과 보안 원칙의 관계 (중요 — 승인 필요)

CLAUDE.md 3.2·3.3은 "정답은 서버에만, 판정은 서버에서"를 요구한다. Sprint 2는 서버가 없으므로 다음 **임시 예외**를 명시한다.

- mock 단계에서는 정답·힌트가 클라이언트 fixtures에 존재하고 판정도 클라이언트에서 실행된다.
- 단, 판정 함수(`checkAnswer`)와 힌트 해제 판정(`shouldUnlockHint` — 같은 학생·같은 문제 오답 `HINT_UNLOCK_WRONG_COUNT`회)은 **데이터 접근 계층 안에만** 둔다. 화면 컴포넌트가 정답 원문을 직접 읽지 않는다.
- Supabase 연결 시 이 함수들의 구현이 서버 호출로 교체되고, fixtures의 정답 필드는 서버 시드로 이동한다. **이 임시 예외는 mock 단계에 한정**되며 CLAUDE.md의 최종 기준은 유지된다.
- 이 예외는 Sprint 2 계획 승인에 포함해 사용자 승인을 받는다.

## 4. 상태 관리 범위

- 기본 수단: **React state + Context** (게임 편집 상태 1개, 학생 플레이 상태 1개)
- 전역 상태 라이브러리(zustand 등)는 설치하지 않는다. Context로 부족하다고 판단되면 근거와 함께 **별도 승인** 요청.
- 서버 상태 캐시 라이브러리는 mock 단계에서 불필요.

## 5. 진행 규칙 (rules.ts 상수 기준 — 값 재정의 금지)

- 방 `ROOM_COUNT`(3)개 순차 진행, 방 안 자유 탐색
- 방당 문제 `MIN_QUESTIONS_PER_ROOM`(3)~`MAX_QUESTIONS_PER_ROOM`(5)개, 전부 필수
- 재도전 무제한, 같은 학생·같은 문제 오답 `HINT_UNLOCK_WRONG_COUNT`(2)회 → 힌트 `HINTS_PER_QUESTION`(1)개 해제
- 현재 방 전 문제 해결 → 출구 개방 → 다음 방
- (팀전 `MIN_TEAM_COUNT`~`MAX_TEAM_COUNT`(2~6), 세션 최대 `MAX_STUDENTS_PER_SESSION`(30)은 Sprint 2 범위 밖 — 타입 설계에만 반영)

## 6. 테스트 전략

- **Vitest**: 판정 함수(정답/오답), 힌트 해제 조건(2회 오답, 개인 기준), 출구 개방 조건(전 문제 해결), fixtures가 rules 상수를 준수하는지
- **Playwright**: 학생 mock 플레이 관통(입장→방1~3→탈출→결과), 교사 mock 제작 관통(새 게임→문제 입력→미리보기)
- mock 구현체를 그대로 테스트 대상으로 쓴다 — Supabase 교체 후에도 같은 계약 테스트를 서버 구현체에 재사용하는 것을 목표로 한다.

## 7. Sprint 2에서 하지 않는 것

- 실제 네트워크 통신, Supabase 패키지·연결 코드, DB 스키마
- 교사 로그인, 실시간 학생 목록, 영구 저장(게시·버전 스냅샷)
- `src/server/*` 구현 (폴더 골격 유지)
