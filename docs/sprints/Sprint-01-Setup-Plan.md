# Sprint 1 — 프로젝트 셋업 계획

프로젝트를 **개발 가능한 상태**로 만드는 스프린트. 게임 기능은 하나도 구현하지 않는다.

| 항목 | 내용 |
| --- | --- |
| 스프린트 | Sprint 1 (프로젝트 셋업) |
| 작성일 | 2026-08-02 |
| 상태 | **승인됨** (2026-08-02 — 계획 및 추가 의존성 A-1~A-7 전체 승인) |
| 기준 요구사항 | Sprint 0에서 확정한 [../01_REQUIREMENTS_DECISIONS.md](../01_REQUIREMENTS_DECISIONS.md) (D-01 ~ D-12) |
| 선행 문서 | [PROJECT.md](../../PROJECT.md) · [CLAUDE.md](../../CLAUDE.md) · [README.md](../../README.md) |

> **문서 관계:** 기존 [../archive/02_SPRINT_00_PLAN_REPLACED.md](../archive/02_SPRINT_00_PLAN_REPLACED.md)는 같은 목표를 "Sprint 0"이라는 이름으로 다룬 이전 계획이며 승인되지 않았다. 스프린트 번호가 재정의되어(Sprint 0 = 요구사항 확정, Sprint 1 = 셋업) **이 문서가 그 계획을 대체한다.** 기존 문서는 이력으로 남긴다. 내용 중 유효한 검토 결과(환경 확인, 위험 분석)는 이 문서에 승계했다.

> 이 문서는 계획이다. **승인 전에는 `npm install`, `create-next-app`, 코드 생성, 라이브러리 설치, Git 변경을 하지 않는다.**

> **일정 변경 (2026-08-03):** **Step 5(Supabase 연결)는 UI와 기본 게임 흐름 구현 이후로 이연한다.** Sprint 1의 진행 순서는 **Step 4 → Step 6 → Step 7 → Step 8**이다. 이연 원칙과 완료 조건 조정은 [§12](#12-일정-변경--supabase-연결-이연-2026-08-03)를 본다.

---

## 1. 현재 프로젝트 상태 (2026-08-02 승인 시점 기준으로 갱신)

### 1.1 저장소

| 항목 | 상태 |
| --- | --- |
| Git 저장소 | 초기화됨. `main` 브랜치, 커밋 2개. 최신 커밋 `d7c6a68` — 문서 구조 개편(tasks/·changelog/·decisions/·docs/ 재편) 반영 |
| 원격 | `origin/main` 존재, `d7c6a68`까지 push 완료 (동기화 상태) |
| 미커밋 파일 | 없음 — 작업 트리 깨끗함 |
| `safe.directory` | **등록 완료** (2026-08-02) — Git 명령 정상 동작 |

### 1.2 파일 구성

| 항목 | 상태 |
| --- | --- |
| 문서 세트 v2.0 (`PROJECT.md`, `CLAUDE.md`, `README.md`, `docs/`, `tasks/`, `changelog/`, `decisions/`, `scripts/`) | 완료 — `d7c6a68`로 커밋됨 |
| `assets/` (backgrounds, objects, characters, ui, audio, icons) | 빈 폴더 + `.gitkeep` |
| `public/`, `supabase/`, `tests/` | 빈 폴더 + `.gitkeep` |
| 애플리케이션 코드 | **없음** — `package.json`, 설정 파일, 소스 코드 일체 없음 |

### 1.3 개발 환경 (Sprint 0 계획 검토 시 확인, 승계)

| 도구 | 버전 | 판정 |
| --- | --- | --- |
| Node.js | v24.15.0 | 사용 가능 |
| npm | 11.12.1 | 사용 가능 — **패키지 매니저는 npm으로 확정** |
| Git | 2.54.0.windows.1 | 사용 가능 |
| Docker | 없음 | Sprint 1에서는 불필요 (클라우드 Supabase 사용) |
| Supabase CLI | 없음 | devDependency로 설치 예정 (§3.2) |

### 1.4 최우선 위험 — Z: 네트워크 드라이브

프로젝트가 네트워크 드라이브(Z:)에 있다. **Sprint 1의 첫 관문은 아래 검증이다.**

| # | 확인 항목 | 결과 (2026-08-02 검증) |
| --- | --- | --- |
| W-1 | `npm install`이 Z: 드라이브에서 정상 완료되는가 (임시 폴더에서 소규모로 선검증) | **실패 확정** — node.exe가 Z:에서 파일 생성·쓰기 자체가 EPERM으로 거부됨. `npm init`·`npm install` 모두 불가. 동일 시험이 로컬 C:에서는 전부 성공 → Z: 드라이브 고유 문제. git.exe·PowerShell 쓰기는 정상이므로 node 계열 프로세스에 대한 차단(보안 소프트웨어 또는 드라이브 정책)으로 추정 |
| W-2 | Next.js 개발 서버 파일 감시(HMR)가 동작하는가 | **통과** (2026-08-02, 로컬 이전 후) — 로컬 경로에서 dev 서버 기동 중 `page.tsx` 수정 시 153ms에 재컴파일 확인 |
| W-3 | Git `safe.directory` 등록 | **완료** — 2026-08-02 등록됨 |

> **판정: R-1 발생.** 계획 §9 R-1의 대응에 따라 **프로젝트를 로컬 디스크로 이전하는 결정이 필요하다.** Z:는 문서·자산 보관과 git 원격 동기화 용도로는 정상 동작한다.

---

## 2. Sprint 1에서 생성할 파일과 폴더

### 2.1 설정 파일 (프로젝트 루트)

| 파일 | 내용 |
| --- | --- |
| `package.json` | 의존성 + 스크립트: `dev` `build` `start` `lint` `format` `test` `test:e2e` `prepare`(husky) |
| `package-lock.json` | 잠금 파일 |
| `tsconfig.json` | `strict: true`, `@/*` 별칭 |
| `next.config.ts` | Next.js 설정 |
| `eslint.config.mjs` | ESLint (flat config, `eslint-config-next` + `eslint-config-prettier`) |
| `.prettierrc` / `.prettierignore` | Prettier 설정 |
| `postcss.config.mjs` | Tailwind용 |
| `tailwind.config.ts` | Tailwind v3인 경우만. **v4면 CSS 기반 설정** (착수 시 실물 확인) |
| `vitest.config.ts` | 대상: `tests/unit/` |
| `playwright.config.ts` | 대상: `tests/e2e/`, `webServer`로 dev 서버 자동 기동 |
| `.husky/pre-commit` | `lint-staged` 실행 |
| `lint-staged` 설정 | `package.json` 내 — staged 파일에 ESLint + Prettier |
| `.gitignore` | `node_modules/`, `.next/`, `.env*.local`, `/coverage`, `/test-results`, `/playwright-report` |
| `.gitattributes` | `* text=auto eol=lf` (CRLF 경고 해소) |
| `.env.example` | 변수 이름만, 값 없음 (§5) |
| `.env.local` | 실제 값 — **커밋 금지** |

### 2.2 애플리케이션 파일 (최소한)

| 파일 | 내용 |
| --- | --- |
| `src/app/layout.tsx` | 루트 레이아웃 (`lang="ko"`) |
| `src/app/page.tsx` | 임시 첫 페이지 |
| `src/app/globals.css` | Tailwind 진입점 |
| `src/lib/supabase/client.ts` | ~~브라우저 Supabase 클라이언트 (anon 키)~~ — **이연** (§12) |
| `src/server/supabase/server.ts` | ~~서버 Supabase 클라이언트 — 최상단 `import 'server-only'`~~ — **이연** (§12) |
| `src/lib/constants/rules.ts` | 규칙 상수 8개 (§2.4) |

### 2.3 테스트 파일 (예시 각 1개)

| 파일 | 내용 |
| --- | --- |
| `tests/unit/rules.test.ts` | 상수 값 검증 (`ROOM_COUNT === 3`, `MIN <= MAX` 등) |
| `tests/e2e/smoke.spec.ts` | 첫 페이지 200 응답 확인 |

### 2.4 규칙 상수 (`src/lib/constants/rules.ts` 한 곳에만)

| 상수 | 값 | 근거 |
| --- | --- | --- |
| `ROOM_COUNT` | 3 | PROJECT.md 4.1 |
| `MIN_QUESTIONS_PER_ROOM` | 3 | PROJECT.md 4.1 |
| `MAX_QUESTIONS_PER_ROOM` | 5 | PROJECT.md 4.1 |
| `HINT_UNLOCK_WRONG_COUNT` | 2 | PROJECT.md 4.2 |
| `HINTS_PER_QUESTION` | 1 | D-10 |
| `MIN_TEAM_COUNT` | 2 | D-07 |
| `MAX_TEAM_COUNT` | 6 | D-07 |
| `MAX_STUDENTS_PER_SESSION` | 30 | PROJECT.md 1 |

- **팀 정원 상수는 만들지 않는다.** (D-07 — 균등 배정)
- **문제 유형·과목·학년은 상수로 만들지 않는다.** DB 마스터 데이터다. (CLAUDE.md 3.4)

### 2.5 폴더 자리 (한 줄 README.md만, 구현 없음)

| 폴더 | 용도 |
| --- | --- |
| `src/app/(teacher)/` | 교사 화면 — 인증 필요 (이후 스프린트) |
| `src/app/(play)/` | 학생 플레이 — 익명 참여 (이후 스프린트) |
| `src/app/api/` | Route Handlers |
| `src/server/grading/` | 채점 로직 (서버 전용, 이후 스프린트) |
| `src/server/progress/` | 진행 상태 판정 (서버 전용, 이후 스프린트) |
| `src/server/auth/` | 권한 확인 |
| `src/features/builder/` | 제작기 — 자유 배치 (이후 스프린트) |
| `src/features/play/` | 학생 플레이 화면 (이후 스프린트) |
| `src/features/session/` | 세션·개인전·팀전 (이후 스프린트) |
| `src/features/library/` | 콘텐츠 공개·검색·복제 (이후 스프린트) |
| `src/components/ui/` | 공용 UI 컴포넌트 |
| `src/types/` | 공용 타입 (DB 타입 생성물 포함) |
| `src/lib/utils/` | 유틸 |
| `supabase/migrations/` | 스키마 + RLS (이후 스프린트) |
| `supabase/seed/` | 자산·과목·학년 마스터 데이터 |

> **선제 추상화 금지** — 인터페이스, 추상 클래스, 플러그인 구조를 미리 설계하지 않는다. 폴더와 한 줄 설명까지만 둔다. (CLAUDE.md 2.2)

### 2.6 갱신할 기존 파일

| 파일 | 변경 |
| --- | --- |
| `README.md` | "설치 및 실행" 빈 섹션 7개를 실제 명령으로 채움. "현재 개발 상태" 표 갱신 |
| 이 문서 | 착수 시 확인 항목(§3.4) 결과와 확정 버전 기록 |

### 2.7 Sprint 1에서 만들지 않는 것

- DB 스키마 마이그레이션 (`supabase/migrations/*.sql`)
- 교사 인증 화면·미들웨어
- 채점 로직, 제작기 캔버스, 세션·팀전, 콘텐츠 공유 — 전부 폴더 자리만
- 디자인 시스템, 컴포넌트 라이브러리
- CI 워크플로(`.github/workflows/`), Vercel 배포 설정

---

## 3. 기술 스택 최종 확정

### 3.1 확정 — 기본 후보 그대로 채택

`PROJECT.md` 12장과 이번 지시의 기본 후보를 그대로 확정한다.

| 영역 | 패키지 | 비고 |
| --- | --- | --- |
| 프레임워크 | `next` (App Router) | |
| UI | `react`, `react-dom` | |
| 언어 | `typescript` | `strict: true` 필수 |
| 스타일 | `tailwindcss` | v3/v4 여부는 착수 시 실물 확인 (§3.4 V-2) |
| 린트 | `eslint`, `eslint-config-next` | `create-next-app` 기본 포함 |
| 포맷 | `prettier` | |
| Git 훅 | `husky` | pre-commit에서 lint-staged 실행 |
| 스테이징 검사 | `lint-staged` | staged 파일만 ESLint + Prettier |
| 단위·통합 테스트 | `vitest` | |
| E2E 테스트 | `@playwright/test` | |
| 백엔드·인증·실시간 | `@supabase/supabase-js` | Realtime 내장, 별도 패키지 없음 |
| 데이터베이스 | PostgreSQL (Supabase 관리형) | 패키지 설치 대상 아님 |

패키지 매니저: **npm** (이미 설치됨, 추가 도구 불필요).

### 3.2 승인 요청 — 추가 의존성 7개

기본 후보 밖이므로 CLAUDE.md 2.3에 따라 승인을 받는다. **승인 없이는 설치하지 않는다.**

| # | 패키지 | 용도 | 필요한 이유 |
| --- | --- | --- | --- |
| A-1 | `@supabase/ssr` | App Router에서 서버·클라이언트 Supabase 클라이언트 생성 | 쿠키 기반 세션 처리에 필요. 없이 직접 구현하면 인증 세션이 서버 컴포넌트에서 유실된다. Supabase 공식 패키지 |
| A-2 | `server-only` | 서버 전용 모듈이 클라이언트에 import되면 **빌드 실패** | CLAUDE.md 3.2·3.3 "정답을 클라이언트에 노출하지 않는다"를 규칙이 아니라 **빌드 오류로 강제**. Next.js 공식, 런타임 코드 없음 |
| A-3 | `@vitejs/plugin-react` | Vitest에서 React 컴포넌트 테스트 | Vitest 실행에 필요 |
| A-4 | `vite-tsconfig-paths` | Vitest에서 `@/` 경로 별칭 해석 | 없으면 테스트에서 import 경로가 깨진다 |
| A-5 | `supabase` (CLI, devDep) | 마이그레이션 파일 관리 | 다음 스프린트의 스키마·RLS 작업 준비. Docker는 요구하지 않음 (클라우드 프로젝트에 직접 적용) |
| A-6 | `eslint-config-prettier` | ESLint의 포맷 규칙 비활성화 | ESLint와 Prettier를 같이 쓸 때 규칙 충돌 방지. 이것이 없으면 두 도구가 서로 다른 포맷을 강제한다 |
| A-7 | `prettier-plugin-tailwindcss` | Tailwind 클래스 정렬 | 클래스 순서를 자동 통일. 코드 리뷰 소음 감소. **선택 사항 — 제외해도 무방** |

**이 7개 외에는 아무것도 추가하지 않는다.** 상태 관리, UI 컴포넌트, 폼, 날짜 라이브러리는 필요해지는 시점에 별도 승인을 받는다.

> **일정 변경 (2026-08-03):** A-1(`@supabase/ssr`)·A-2(`server-only`)·A-5(`supabase` CLI)는 **승인은 유지하되 설치를 이연**한다. Supabase 연결 시점(§12)에 설치한다. A-3·A-4(Vitest 관련)·A-6·A-7(Prettier 관련)은 예정대로 진행한다.

### 3.3 명시적으로 넣지 않는 것

- **LLM/AI SDK 일체** — CLAUDE.md 3.1 (`openai`, `@anthropic-ai/sdk`, `langchain` 등 전부 금지)
- 결제 SDK — D-12 (유료 거래 제외)
- 파일 업로드 라이브러리 — D-11 (교사 업로드 없음)

### 3.4 착수 시 실물 확인 항목

버전을 문서에 미리 못 박지 않는다. 착수 시점에 확인하고 결과를 이 문서에 기록한다.

| # | 확인 항목 | 확인 방법 |
| --- | --- | --- |
| V-1 | Next.js 최신 안정 버전과 Node 24 지원 | `npm view next version`, 릴리스 노트 |
| V-2 | `create-next-app`이 깔아 주는 **Tailwind 메이저 버전** (v3/v4) | 생성된 `package.json` |
| V-3 | Supabase API 키 명칭 (`anon`/`service_role` vs `publishable`/`secret`) | Supabase 대시보드 실물 |
| V-4 | `@supabase/ssr` 최신 버전과 쿠키 API 시그니처 | 공식 문서 |
| V-5 | Vitest 최신 버전 | `npm view vitest version` |
| V-6 | Playwright 브라우저 바이너리 설치 성공 여부 | `npx playwright install` (실패 시 Chromium만) |
| V-7 | Node 24와 각 패키지 호환성 | `npm install` 경고 확인 |
| V-8 | Husky가 Z: 드라이브의 Git 훅에서 정상 동작하는가 | pre-commit 훅 실제 실행 |

#### 확인 결과 기록 (2026-08-02, Step 1 착수 시점)

| # | 결과 |
| --- | --- |
| V-1 | Next.js **16.2.12** (create-next-app 동일 버전). Node v24.15.0에서 설치·기동 정상 |
| V-2 | Tailwind **v4.3.3** — CSS 기반 설정 채택 (`postcss.config.mjs` + `globals.css`의 `@import "tailwindcss"`). `tailwind.config.ts`는 만들지 않음 |
| V-5 | Vitest 최신 4.1.10, @playwright/test 1.62.1 (설치는 Step 7) |
| V-7 | `npm install` 106초 완료, peer dependency 경고 없음. React 19.2.4, TypeScript 5.9.3 |
| 참고 | 작업 위치가 로컬 C:로 이전되어 V-8의 "Z: 드라이브" 조건은 로컬 경로 기준으로 확인한다 |

---

## 4. 폴더 구조

```
classquest-builder/
├─ src/
│  ├─ app/                        Next.js App Router
│  │  ├─ layout.tsx               루트 레이아웃 (lang="ko")
│  │  ├─ page.tsx                 임시 첫 페이지
│  │  ├─ globals.css              Tailwind 진입점
│  │  ├─ (teacher)/               교사 화면 — 인증 필요        [자리만]
│  │  ├─ (play)/                  학생 플레이 — 익명 참여      [자리만]
│  │  └─ api/                     Route Handlers               [자리만]
│  │
│  ├─ server/                     ★ 서버 전용. 클라이언트 import 시 빌드 실패
│  │  ├─ supabase/                서버 클라이언트, service_role 접근
│  │  ├─ grading/                 채점 로직                    [자리만]
│  │  ├─ progress/                진행 상태 판정               [자리만]
│  │  └─ auth/                    권한 확인                    [자리만]
│  │
│  ├─ features/                   기능 단위 묶음 (전부 자리만)
│  │  ├─ builder/                 제작기 (자유 배치)
│  │  ├─ play/                    학생 플레이 화면
│  │  ├─ session/                 세션·개인전·팀전
│  │  └─ library/                 콘텐츠 공개·검색·복제
│  │
│  ├─ lib/
│  │  ├─ constants/               ★ 규칙 상수 (한 곳에만)
│  │  ├─ supabase/                브라우저 클라이언트 (anon 키)
│  │  └─ utils/                   [자리만]
│  │
│  ├─ components/ui/              공용 UI 컴포넌트             [자리만]
│  └─ types/                      공용 타입                    [자리만]
│
├─ supabase/
│  ├─ migrations/                 스키마 + RLS                 [자리만]
│  └─ seed/                       마스터 데이터                [자리만]
│
├─ tests/
│  ├─ unit/                       Vitest (예시 1개)
│  └─ e2e/                        Playwright (예시 1개)
│
├─ assets/                        원본 리소스 (기존 유지)
├─ docs/                          문서 (기존 유지)
├─ public/                        정적 파일 (기존 유지)
└─ .husky/                        Git 훅 (pre-commit → lint-staged)
```

### 4.1 구조의 핵심 — `src/server/`

- 이 아래 모든 파일은 최상단에 `import 'server-only'`를 둔다.
- 클라이언트 컴포넌트가 실수로 import하면 **빌드가 실패한다.**
- 정답 판정, 진행 판정, `service_role` 사용이 전부 이 안에만 있게 된다.
- CLAUDE.md 3.2·3.3(정답 비노출·서버 판정)을 사람의 주의력이 아니라 **도구로 강제**한다.

### 4.2 `src/` 디렉터리를 쓰는 이유

앱 코드와 기존의 `assets/`·`docs/`·`supabase/`·`tests/`를 명확히 분리한다. `create-next-app`의 `--src-dir` 옵션을 쓴다.

---

## 5. 환경 변수 (`.env.example`)

`.env.example`은 변수 이름만 담아 커밋하고, 실제 값은 `.env.local`에만 둔다.

### 5.1 Sprint 1에 필요한 변수

| 변수명 | 노출 | 용도 | 비고 |
| --- | --- | --- | --- |
| `NEXT_PUBLIC_SUPABASE_URL` | 공개 | Supabase 프로젝트 URL | 브라우저 노출 정상 |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | 공개 | 익명 키 (RLS 적용 대상) | 브라우저 노출 정상. **RLS 없으면 이 키로 전체 데이터가 열린다** |
| `SUPABASE_SERVICE_ROLE_KEY` | **비밀** | RLS 우회 서버 작업 | **`NEXT_PUBLIC_` 절대 금지.** `src/server/` 안에서만 읽는다 |

> V-3 확인 결과 키 명칭이 `publishable`/`secret` 계열이면 변수명을 그에 맞춰 확정하고 이 표를 갱신한다.

### 5.2 이후 스프린트에 추가될 변수 (지금은 만들지 않음)

| 변수명 | 시점 |
| --- | --- |
| `NEXT_PUBLIC_SITE_URL` | 인증 리디렉션 필요 시 |
| `DATABASE_URL` | 마이그레이션 도구 사용 시 |

### 5.3 안전 규칙

- 커밋 전 `git status`로 `.env.local`이 추적되지 않음을 **직접 확인**한다.
- `service_role` 키를 클라이언트 코드, `NEXT_PUBLIC_*`, 로그, 에러 메시지에 넣지 않는다.
- 키가 한 번이라도 저장소에 올라가면 **즉시 재발급**한다. 커밋 삭제로는 해결되지 않는다.
- 빌드 산출물(`.next/`)에서 `service_role` 키 문자열이 검색되지 않는지 확인한다.

---

## 6. Git 브랜치 전략

1인 개발 + 3개월 MVP에 맞춘 최소 구성. GitFlow 같은 무거운 전략은 쓰지 않는다.

### 6.1 브랜치

| 브랜치 | 역할 |
| --- | --- |
| `main` | 항상 동작하는 상태. 직접 커밋하지 않는다 |
| `feat/*` | 기능 개발 |
| `fix/*` | 버그 수정 |
| `docs/*` | 문서만 변경 |
| `chore/*` | 설정·빌드·의존성 |

`develop` 브랜치는 두지 않는다. 1인 개발에서는 병합 부담만 늘고 얻는 것이 없다.

### 6.2 규칙

- `main` 직접 커밋 금지. 항상 브랜치 → PR → **Squash merge** → 브랜치 삭제.
- 브랜치 하나 = 작업 하나.
- 병합 전 확인: `npm run build`, `npm run lint`, `npm run test` 통과.
- pre-commit 훅(husky + lint-staged)이 커밋 시점에 ESLint·Prettier를 강제한다.
- 커밋 메시지: Conventional Commits (`feat | fix | docs | chore | test | refactor`).

### 6.3 Sprint 1 브랜치

```
chore/sprint-1-setup
```

Sprint 1 작업 전체를 이 브랜치에서 진행하고, 완료 후 PR로 `main`에 병합한다.

### 6.4 착수 시 함께 처리할 Git 사항 (승인 후)

| 항목 | 내용 |
| --- | --- |
| `safe.directory` 등록 | **완료** (2026-08-02) |
| 미커밋 문서 정리 | **완료** — 문서 구조 개편 전체를 `d7c6a68`로 `main`에 커밋·push함 (사용자 지시로 main 직접 커밋. 본 계획의 브랜치 규칙은 이후 작업부터 적용) |

---

## 7. 작업 순서 (승인 후 진행)

| 단계 | 내용 | 예상 |
| --- | --- | --- |
| Step 0 | Z: 드라이브 검증(W-1·W-2), `safe.directory` 등록, 브랜치 생성 | 30분 |
| Step 1 | `create-next-app` 스캐폴딩 (TypeScript·Tailwind·ESLint·App Router·`src/`·`@/*`) — **기존 README.md 덮어쓰기 주의** | 30분 |
| Step 2 | 설정 고정 — strict, `.gitignore`, `.gitattributes`, `.env.example`/`.env.local`, Prettier | 40분 |
| Step 3 | Husky + lint-staged 설정, pre-commit 동작 확인 (V-8) | 30분 |
| Step 4 | 폴더 골격 생성 (§4, 한 줄 README 포함) | 30분 |
| Step 5 | ~~Supabase 클라우드 프로젝트 생성·연결 확인 (§3.2 A-1·A-2 사용)~~ — **이연** (2026-08-03, §12) | - |
| Step 6 | 규칙 상수 파일 생성 (§2.4) | 20분 |
| Step 7 | Vitest·Playwright 설정 + 예시 테스트 각 1개 통과 | 1시간 30분 |
| Step 8 | 전체 검증(dev·build·lint·tsc·test·e2e), README 채우기, 확인 결과 기록, PR | 40분 |

**예상 총 소요: 6시간 내외.** 각 단계 종료 시 결과를 보고하고 다음으로 넘어간다. (CLAUDE.md 2.1)

---

## 8. 완료 조건

### 8.1 실행 검증

| # | 조건 | 확인 명령 |
| --- | --- | --- |
| C-1 | 개발 서버 기동, 첫 페이지 열림 | `npm run dev` |
| C-2 | 프로덕션 빌드 성공 | `npm run build` |
| C-3 | 린트 통과 | `npm run lint` |
| C-4 | 타입 오류 없음 | `npx tsc --noEmit` |
| C-5 | Vitest 예시 통과 | `npm run test` |
| C-6 | Playwright 예시 통과 | `npm run test:e2e` |
| C-7 | pre-commit 훅이 실제로 동작 | 테스트 커밋으로 확인 |

### 8.2 구조·보안 검증

| # | 조건 |
| --- | --- |
| C-8 | §4 폴더 구조 생성, 각 폴더에 용도 README |
| C-9 | `src/server/` 파일에 `server-only` 적용 — 클라이언트에서 import 시 **빌드 실패를 직접 확인** — **이연** (§12, Supabase 연결 시점에 검증) |
| C-10 | 규칙 상수가 `src/lib/constants/rules.ts` 한 곳에만 존재 |
| C-11 | `tsconfig.json` `strict: true` |
| C-12 | `git status`에 `.env.local` 미출현 |
| C-13 | `SUPABASE_SERVICE_ROLE_KEY`에 `NEXT_PUBLIC_` 접두사 없음 |
| C-14 | `.env.example`에 실제 키 값 없음 |
| C-15 | `.next/` 산출물에서 `service_role` 키 문자열 미검출 |

### 8.3 문서·Git 검증

| # | 조건 |
| --- | --- |
| C-16 | `README.md` "설치 및 실행" 실제 명령으로 채움 |
| C-17 | 이 문서에 V-1~V-8 확인 결과·확정 버전 기록 |
| C-18 | `chore/sprint-1-setup` 브랜치에서 작업, PR로 `main` 병합 |

---

## 9. 위험 요소

| # | 위험 | 영향 | 가능성 | 대응 |
| --- | --- | --- | --- | --- |
| R-1 | **Z: 드라이브에서 `npm install` 실패·극심한 지연** | 스프린트 중단 | **높음** | Step 0에서 최우선 검증. 실패 시 로컬 디스크 이전을 즉시 논의 |
| R-2 | HMR(파일 감시) 미동작 | 개발 속도 저하 | 중간 | Step 0에서 검증. 폴링 설정 또는 로컬 이전 |
| R-3 | Tailwind v4 스캐폴딩으로 설정 방식 상이 | 설정 시간 추가 | 중간 | V-2 확인. v4면 CSS 기반 설정을 따르고 v3로 억지로 내리지 않음 |
| R-4 | Supabase 키 명칭 변경 | 문서·실물 불일치 | 중간 | V-3 실물 확인 후 갱신 |
| R-5 | **`service_role` 키 실수 커밋** | **심각 — 전체 DB 노출** | 낮음 | C-12~C-15 다중 확인. 발생 시 즉시 재발급 |
| R-6 | Playwright 브라우저 다운로드 실패 | E2E 지연 | 중간 | 실패 시 Chromium만 설치 |
| R-7 | `create-next-app`이 기존 `README.md` 덮어씀 | 문서 유실 | 중간 | Step 1 직후 확인. Git에서 복원 가능 |
| R-8 | Husky 훅이 네트워크 드라이브에서 오동작 | 커밋 검사 누락 | 중간 | V-8에서 실제 커밋으로 확인. 실패 시 수동 `npm run lint` 규칙으로 대체하고 보고 |
| R-9 | 선제 추상화 유혹 (제작기·팀전 인터페이스 미리 설계) | 잘못된 구조 제거 비용 | 중간 | 폴더 + 한 줄 설명까지만 (§2.5) |
| R-10 | 스프린트 범위 확대 (스키마·인증까지 손댐) | 일정 초과 | 중간 | §2.7 "만들지 않는 것" 준수 |

---

## 10. 승인 요청

아래 3가지에 대한 승인이 필요합니다.

| # | 확인이 필요한 사항 |
| --- | --- |
| 1 | **추가 의존성 7개** (§3.2, A-1~A-7) — 특히 `@supabase/ssr`(인증 세션), `server-only`(정답 유출 방지 빌드 강제). A-7(Tailwind 클래스 정렬)은 선택이므로 제외 가능 |
| 2 | **`src/` 디렉터리 구조** (§4) — 기존 `assets/`·`docs/`와 앱 코드 분리 |
| 3 | **Z: 드라이브 위험 대응** (R-1) — Step 0 검증 실패 시 로컬 디스크 이전을 논의해야 합니다 |

승인해 주시면 Step 0(사전 검증)부터 시작하고, 각 단계 결과를 보고하겠습니다.


---

## 11. 구현 체크리스트

승인 후 Claude Code는 아래 항목을 순서대로 진행하고, 각 단계 종료 시 결과를 보고한다.

- [x] Z: 드라이브에서 npm 설치·파일 감시·Git safe.directory 선검증 — W-1 실패 → 로컬 C: 이전으로 해소, W-2·W-3 통과 (Step 0, 2026-08-02)
- [x] Next.js App Router 프로젝트 초기화 — 16.2.12 (Step 1, 2026-08-02)
- [x] TypeScript strict 및 경로 별칭 확인 (Step 1~2, 2026-08-02)
- [x] Tailwind CSS 실제 설치 버전에 맞춰 설정 — v4.3.3, CSS 기반 (Step 1~2, 2026-08-02)
- [x] ESLint·Prettier 설정 — eslint-config-prettier·prettier-plugin-tailwindcss 포함 (Step 2, 2026-08-02)
- [x] Husky·lint-staged 설정 — 통과·차단 실시험 완료, V-8 통과 (Step 3, 2026-08-02)
- [x] 폴더 골격 생성 — §4·§2.5의 20개 폴더 + 용도 한 줄 README, 선제 추상화 없음 (Step 4, 2026-08-03)
- [ ] ~~Supabase 클라이언트·서버 경계 준비~~ — **이연** (2026-08-03, §12)
- [x] `.env.example` 및 `.gitignore` 검증 — `!.env.example` 추적·`.env.local` 미추적·비밀값 없음 확인 (Step 2, 2026-08-02)
- [ ] Vitest 예시 테스트 통과
- [ ] Playwright smoke 테스트 통과
- [ ] `npm run lint`, `npm run test`, `npm run test:e2e`, `npm run build` 실행
- [ ] 변경 파일·테스트 결과·미완료 항목 보고
- [ ] `tasks/NEXT_TASK.md`·`changelog/Sprint-01.md` 갱신
- [ ] 사용자가 요청한 경우에만 Git commit/push 수행

---

## 12. 일정 변경 — Supabase 연결 이연 (2026-08-03)

Project Owner 결정으로 **Step 5(Supabase 연결) 전체를 UI와 기본 게임 흐름 구현 이후로 이연**한다.

### 원칙

- **Supabase 클라우드 프로젝트를 현재 생성하지 않는다.**
- **실제 키를 현재 발급하거나 어디에도 입력하지 않는다.** (`.env.example`은 변수 이름만 유지)
- **Supabase 패키지(A-1·A-2·A-5)와 연결 코드를 현재 추가하지 않는다.**
- **UI와 기본 게임 흐름은 mock data로 먼저 구현한다.**
- **데이터 접근 계층은 나중에 Supabase로 교체하기 쉽도록 분리해 설계한다.**
- **교사 로그인, 실시간 학생 참여, 데이터 저장을 구현하기 직전에 Supabase를 연결한다.**
- **정식 운영 전에 RLS, 권한 분리, 개인정보 보호, 백업, 요금제를 검토한다.**

### Sprint 1에 미치는 영향

- 진행 순서: Step 4 → **Step 6(규칙 상수) → Step 7(테스트 설정) → Step 8(마무리·PR)**. Step 5는 수행하지 않는다.
- 유지하는 것: `supabase/migrations`·`supabase/seed`·`src/lib/supabase`·`src/server/supabase` 폴더 골격과 README, `.env.example`의 변수 이름 3개 (값 없음).
- 이연되는 완료 조건: C-9(server-only 빌드 실패 검증). C-12~C-15(비밀키 안전 조건)는 "실제 키가 존재하지 않음"으로 현재도 충족된다.
- Supabase 연결 시점이 오면 이 문서의 Step 5 지시와 §3.2 A-1·A-2·A-5 승인을 그대로 사용한다.
