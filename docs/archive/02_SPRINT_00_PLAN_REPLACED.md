# Sprint 0 — 개발 준비 계획

> **⚠️ 대체됨 — 이 문서는 현재 계획이 아니다.**
> 이 문서는 승인되지 않은 이전 계획이며, 스프린트 번호 재정의(Sprint 0 = 요구사항 확정, Sprint 1 = 환경 구축) 이후
> [../sprints/Sprint-01-Setup-Plan.md](../sprints/Sprint-01-Setup-Plan.md)가 이 계획을 대체한다. 이력 보존용으로만 남긴다.

프로젝트 뼈대를 세우는 스프린트. **기능은 하나도 만들지 않는다.**

| 항목 | 내용 |
| --- | --- |
| 스프린트 | Sprint 0 (개발 준비) — 구 번호 체계 기준 |
| 기간 | **1~2일** |
| 작성일 | 2026-08-02 |
| 상태 | **대체됨** → [../sprints/Sprint-01-Setup-Plan.md](../sprints/Sprint-01-Setup-Plan.md) |
| 선행 문서 | [PROJECT.md](../../PROJECT.md) · [../01_REQUIREMENTS_DECISIONS.md](../01_REQUIREMENTS_DECISIONS.md) · [CLAUDE.md](../../CLAUDE.md) |

> 이 문서는 계획이다. 승인 전에는 코드를 생성하지 않는다.

---

## 1. Sprint 0 목표

3개월 일정에서 Sprint 0은 **개발을 시작할 수 있는 상태를 만드는 것**이 전부다. 화면도 기능도 만들지 않는다.

### 1.1 달성할 것

| # | 목표 | 이유 |
| --- | --- | --- |
| G-1 | Next.js + TypeScript + Tailwind 프로젝트가 로컬에서 실행된다 | 이후 모든 작업의 전제 |
| G-2 | Supabase 프로젝트가 생성되고 앱에서 연결이 확인된다 | 1개월차 스키마 작업의 전제 |
| G-3 | Vitest와 Playwright가 각각 예시 1개로 통과한다 | `CLAUDE.md` 5.1 "기능 구현과 테스트는 한 세트" 이행 준비 |
| G-4 | 서버 전용 코드와 클라이언트 코드의 경계가 폴더 구조로 강제된다 | 정답 유출 방지의 구조적 기반 |
| G-5 | 규칙 상수가 한 곳에 모인다 | `CLAUDE.md` 3.4 하드코딩 금지 이행 |
| G-6 | 환경 변수 템플릿과 `.gitignore`가 자리 잡는다 | `service_role` 키 유출 방지 |
| G-7 | 브랜치 전략이 정해지고 Sprint 0 결과가 PR로 병합된다 | 이후 작업 흐름 확정 |

### 1.2 하지 않을 것

`CLAUDE.md` 2.2에 따라 요청 범위를 넘지 않는다. 아래는 **Sprint 0에서 만들지 않는다.**

- **자유 배치 제작기** — 캔버스, 드래그, Undo/Redo. 폴더 자리만 만든다.
- **팀전** — 팀 배정, 팀 진행 로직. 폴더 자리만 만든다.
- **콘텐츠 공유** — 공개, 검색, 미리보기, 복제. 폴더 자리만 만든다.
- DB 테이블 설계와 마이그레이션 (→ 1개월차)
- 교사 인증 화면 (→ 1개월차)
- 채점 로직 (→ 2개월차)
- 디자인 시스템, 색상 팔레트, 컴포넌트 라이브러리
- CI/CD 파이프라인, Vercel 배포 (→ 3개월차)

> **"향후 구현에 방해되지 않는 구조"의 의미**
> 빈 폴더와 `README` 한 줄까지만 둔다. 인터페이스, 추상 클래스, 플러그인 구조를 **미리 설계하지 않는다.**
> 아직 요구가 확정되지 않은 상태의 선제 추상화는 대부분 틀리고, 나중에 걷어내는 비용이 더 크다.

---

## 2. 기술 스택 확정안

`PROJECT.md` 12장의 스택을 그대로 따른다. 아래는 **구체적인 패키지 단위 확정안**이다.

### 2.1 확정 (PROJECT.md 기재 항목)

| 영역 | 패키지 | 비고 |
| --- | --- | --- |
| 프레임워크 | `next` | App Router 사용 |
| UI | `react`, `react-dom` | |
| 언어 | `typescript` | `strict: true` 필수 |
| 스타일 | `tailwindcss` | |
| 백엔드 | `@supabase/supabase-js` | |
| 실시간 | `@supabase/supabase-js` 내장 Realtime | 별도 패키지 없음 |
| 단위 테스트 | `vitest` | |
| E2E | `@playwright/test` | |

### 2.2 승인이 필요한 추가 의존성

`CLAUDE.md` 2.3에 따라 스택 외 의존성은 승인을 받는다. Sprint 0에서 필요한 것은 아래뿐이다.

| 패키지 | 용도 | 필요한 이유 |
| --- | --- | --- |
| `@supabase/ssr` | Next.js App Router에서 서버·클라이언트 Supabase 클라이언트 생성 | App Router의 쿠키 기반 세션 처리에 필요. 이것 없이 직접 구현하면 인증 세션이 서버 컴포넌트에서 유실된다. Supabase 공식 패키지 |
| `server-only` | 서버 전용 모듈이 클라이언트에 import되면 **빌드 실패**시킴 | `CLAUDE.md` 3.2·3.3의 "정답을 클라이언트에 노출하지 않는다"를 규칙이 아닌 **빌드 오류로 강제**한다. Next.js 공식 패키지, 런타임 코드 없음 |
| `@vitejs/plugin-react` | Vitest에서 React 컴포넌트 테스트 | Vitest 실행에 필요 |
| `vite-tsconfig-paths` | Vitest에서 `@/` 경로 별칭 해석 | 없으면 테스트에서 import 경로가 깨진다 |
| `eslint`, `eslint-config-next` | 린트 | `create-next-app`이 기본 포함 |

**이 5개 외에는 Sprint 0에서 아무것도 추가하지 않는다.** 상태 관리 라이브러리, UI 컴포넌트 라이브러리, 폼 라이브러리, 날짜 라이브러리 모두 필요해지는 시점에 별도 승인을 받는다.

### 2.3 명시적으로 넣지 않는 것

- **LLM/AI 관련 SDK 일체** — `CLAUDE.md` 3.1. `openai`, `@anthropic-ai/sdk`, `@google/generative-ai`, `langchain` 등 어떤 것도 설치하지 않는다.
- 결제 관련 SDK — `PROJECT.md` 11장 (유료 거래 제외)
- 파일 업로드 라이브러리 — D-11 (교사 업로드 없음)

---

## 3. 필요한 개발 도구와 버전 확인 항목

### 3.1 현재 환경 (2026-08-02 확인 완료)

| 도구 | 설치된 버전 | 판정 |
| --- | --- | --- |
| Node.js | **v24.15.0** | 사용 가능 (LTS 계열) |
| npm | **11.12.1** | 사용 가능 |
| Git | **2.54.0.windows.1** | 사용 가능 |
| pnpm | 없음 | 불필요 — npm 사용 |
| yarn | 없음 | 불필요 — npm 사용 |
| Docker | 없음 | **후속 확인 필요** (3.3 참고) |
| Supabase CLI | 없음 | **설치 필요** |

**패키지 매니저는 npm으로 확정한다.** 이미 설치돼 있고 추가 설치가 없다. 성능 차이는 이 규모에서 문제되지 않는다.

### 3.2 Sprint 0 착수 시 확인할 항목

버전을 문서에 미리 못 박지 않는다. 아래는 **착수 시점에 실제로 확인하고 결과를 이 문서에 기록**한다.

| # | 확인 항목 | 확인 방법 | 기록할 것 |
| --- | --- | --- | --- |
| V-1 | Next.js 최신 안정 버전과 Node 24 지원 여부 | `npm view next version`, 릴리스 노트 | 설치된 정확한 버전 |
| V-2 | `create-next-app`이 스캐폴딩하는 **Tailwind 메이저 버전** | 생성된 `package.json` 확인 | v3인지 v4인지. v4면 설정 방식이 CSS 기반으로 달라짐 |
| V-3 | Supabase 클라이언트 키 명칭 | Supabase 대시보드 API 설정 | `anon`/`service_role` 인지, 신 명칭(`publishable`/`secret`)인지 |
| V-4 | `@supabase/ssr` 최신 버전과 App Router 연동 방식 | 공식 문서 | 쿠키 처리 API 시그니처 |
| V-5 | Vitest 최신 버전 | `npm view vitest version` | 설치 버전 |
| V-6 | Playwright 브라우저 바이너리 설치 성공 여부 | `npx playwright install --with-deps` | 실패 시 대응 |
| V-7 | Node 24와 각 패키지의 호환성 | `npm install` 경고 확인 | peer dependency 경고 유무 |

> V-2와 V-3은 **실제로 자주 바뀌는 항목**이다. 문서의 기억이 아니라 그 시점의 실물을 보고 확정한다.

### 3.3 Supabase CLI와 Docker

| 선택지 | 내용 | 판단 |
| --- | --- | --- |
| **A. 클라우드 전용** | Supabase 클라우드 프로젝트에 직접 마이그레이션 적용. Docker 불필요 | **Sprint 0 권장.** 준비가 가장 빠르다 |
| B. 로컬 개발 스택 | `supabase start`로 로컬 Postgres 구동. **Docker Desktop 필수** | 1개월차 스키마 작업 때 재검토 |

Sprint 0에서는 **A**로 간다. Supabase CLI는 마이그레이션 파일 관리를 위해 설치하되(`npm i -D supabase`), Docker는 지금 요구하지 않는다.

로컬 스택은 RLS 정책을 반복 검증할 1개월차에 훨씬 유용해진다. 그때 Docker 설치 여부를 다시 판단한다.

### 3.4 Windows / Z: 드라이브 관련 확인

현재 프로젝트가 **네트워크 드라이브(Z:)** 에 있다. 아래를 착수 시 확인한다.

| # | 항목 | 이유 |
| --- | --- | --- |
| W-1 | `npm install`이 Z: 드라이브에서 정상 완료되는지 | `node_modules`는 파일 수가 매우 많다. 네트워크 드라이브에서 극단적으로 느리거나 실패할 수 있다 |
| W-2 | Next.js 개발 서버 파일 감시(HMR)가 동작하는지 | 네트워크 드라이브는 파일 변경 감지가 안 되는 경우가 있다 |
| W-3 | Git `safe.directory` 예외 등록 | 이미 확인된 문제. 매 명령마다 오류 발생 중 |

**W-1 또는 W-2가 실패하면 로컬 디스크로 프로젝트를 옮기는 것을 먼저 결정해야 한다.** 이 판단이 Sprint 0의 첫 관문이다.

---

## 4. Next.js 초기화 절차

각 단계는 순서대로 진행하고, 단계마다 결과를 확인한 뒤 다음으로 넘어간다. (`CLAUDE.md` 2.1)

### Step 0. 사전 확인 — 30분

1. §3.4의 W-1, W-2를 **작은 테스트 프로젝트로 먼저 검증**한다. (임시 폴더에서 `npm init` + 패키지 하나 설치)
2. 실패 시 → 진행을 멈추고 프로젝트 위치를 재논의한다.
3. Git `safe.directory` 등록.
4. 작업 브랜치 생성: `chore/sprint-0-setup`

### Step 1. 프로젝트 스캐폴딩 — 30분

기존 저장소에 이미 문서와 `assets/`가 있으므로, **빈 폴더에 새로 만들고 병합하지 않는다.** 현재 디렉터리에 직접 초기화한다.

```
npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --use-npm
```

| 옵션 | 선택 | 이유 |
| --- | --- | --- |
| TypeScript | 예 | 스택 확정 |
| Tailwind | 예 | 스택 확정 |
| ESLint | 예 | |
| App Router | 예 | `PROJECT.md` 12장 |
| `src/` 디렉터리 | **예** | 앱 코드와 `assets/`·`docs/`·`supabase/`를 명확히 분리 |
| import alias | `@/*` | |
| Turbopack | 확인 후 결정 | V-1에서 기본값 확인 |

**주의:** 기존 `README.md`를 덮어쓰지 않도록 확인한다. 덮어썼다면 Git에서 복원한다.

### Step 2. 설정 고정 — 30분

1. **`tsconfig.json`** — `strict: true` 확인. `create-next-app` 기본값이지만 명시적으로 확인한다. (`CLAUDE.md` 7)
2. **`.gitignore`** — `node_modules/`, `.next/`, `.env*.local`, `/coverage`, `/test-results`, `/playwright-report` 포함 확인
3. **`.gitattributes`** — `* text=auto eol=lf` 로 줄바꿈 고정 (현재 CRLF 경고 발생 중)
4. **`.env.example`** 작성 (§6)
5. **`.env.local`** 작성 — Git에 올라가지 않음을 반드시 확인

### Step 3. 폴더 골격 생성 — 30분

§5의 구조대로 폴더와 `.gitkeep`을 만든다. **각 폴더에 한 줄짜리 `README.md`를 두어 용도를 남긴다.** 빈 폴더만 있으면 다음 스프린트에서 용도를 잊는다.

### Step 4. Supabase 연결 — 1시간

1. Supabase 클라우드 프로젝트 생성 (리전: 한국에서 가까운 곳)
2. API 키 확인 (V-3)
3. `.env.local`에 값 입력
4. `@supabase/supabase-js`, `@supabase/ssr` 설치
5. 클라이언트 생성 코드 작성
   - `src/lib/supabase/client.ts` — 브라우저용 (anon/publishable 키)
   - `src/server/supabase/server.ts` — 서버용, **`server-only` import 필수**
6. **연결 확인** — 임시 페이지에서 Supabase 연결 상태만 확인하고, 확인 후 **그 페이지를 삭제**한다

> `service_role` 키는 `src/server/` 아래에서만 읽는다. `NEXT_PUBLIC_` 접두사를 절대 붙이지 않는다. (`CLAUDE.md` 4.1)

### Step 5. 상수 파일 생성 — 20분

`src/lib/constants/rules.ts` 하나에 규칙 상수를 모은다. (`CLAUDE.md` 3.4)

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

**팀 정원 상수는 만들지 않는다.** (D-07 — 균등 배정이므로 정원 개념이 없다)
**문제 유형·과목·학년은 상수로 만들지 않는다.** DB 마스터 데이터다. (`CLAUDE.md` 3.4)

### Step 6. 테스트 환경 — 1시간 30분

**Vitest**
1. `vitest`, `@vitejs/plugin-react`, `vite-tsconfig-paths` 설치
2. `vitest.config.ts` 작성 — 테스트 대상은 `tests/unit/`
3. **예시 테스트 1개** — §5.5 상수 파일 값 검증 (예: `MIN <= MAX`, `ROOM_COUNT === 3`)
4. `npm run test` 통과 확인

**Playwright**
1. `@playwright/test` 설치, `npx playwright install`
2. `playwright.config.ts` 작성 — 테스트 대상은 `tests/e2e/`, `webServer`로 dev 서버 자동 기동
3. **예시 테스트 1개** — 첫 페이지가 200으로 열리는지
4. `npm run test:e2e` 통과 확인

### Step 7. 검증과 정리 — 40분

1. `npm run dev` — 개발 서버 정상 기동
2. `npm run build` — 프로덕션 빌드 성공
3. `npm run lint` — 통과
4. `npm run test`, `npm run test:e2e` — 통과
5. **`git status`로 `.env.local`이 추적되지 않음을 확인**
6. `README.md`의 "설치 및 실행" 빈 섹션을 실제 명령으로 채운다
7. 이 문서(`02_SPRINT_00_PLAN_REPLACED.md`)에 V-1~V-7 확인 결과를 기록
8. 커밋 → PR → `main` 병합

**예상 총 소요: 5시간 30분 ~ 6시간.** 문제 발생 여유를 포함해 1~2일 범위에 든다.

---

## 5. 예정 폴더 구조

```
classquest-builder/
├─ src/
│  ├─ app/                        Next.js App Router
│  │  ├─ layout.tsx
│  │  ├─ page.tsx
│  │  ├─ (teacher)/               교사 화면 — 인증 필요       [Sprint 1~]
│  │  ├─ (play)/                  학생 플레이 — 익명 참여     [Sprint 3~]
│  │  └─ api/                     Route Handlers
│  │
│  ├─ server/                     ★ 서버 전용. 클라이언트 import 금지
│  │  ├─ supabase/                서버 클라이언트, service_role 접근
│  │  ├─ grading/                 채점 로직                   [Sprint 4~]
│  │  ├─ progress/                진행 상태 판정              [Sprint 4~]
│  │  └─ auth/                    권한 확인
│  │
│  ├─ features/                   기능 단위 묶음
│  │  ├─ builder/                 제작기 (자유 배치)          [Sprint 2~]
│  │  ├─ play/                    학생 플레이 화면            [Sprint 3~]
│  │  ├─ session/                 세션·개인전·팀전            [Sprint 5~]
│  │  └─ library/                 콘텐츠 공개·검색·복제       [Sprint 6~]
│  │
│  ├─ lib/
│  │  ├─ constants/               ★ 규칙 상수 (한 곳에만)
│  │  ├─ supabase/                브라우저 클라이언트
│  │  └─ utils/
│  │
│  ├─ components/ui/              공용 UI 컴포넌트
│  └─ types/                      공용 타입 (DB 타입 생성물 포함)
│
├─ supabase/
│  ├─ migrations/                 스키마 + RLS 정책           [Sprint 1~]
│  └─ seed/                       자산·과목·학년 마스터 데이터
│
├─ tests/
│  ├─ unit/                       Vitest
│  └─ e2e/                        Playwright
│
├─ assets/                        원본 리소스 (기존)
├─ docs/                          문서 (기존)
└─ public/                        정적 파일
```

### 5.1 `src/server/` 를 따로 두는 이유

이 폴더가 이번 구조의 핵심이다.

- 이 아래 모든 파일은 최상단에 `import 'server-only'` 를 둔다.
- 클라이언트 컴포넌트가 실수로 import하면 **빌드가 실패한다.**
- 정답 판정(`grading/`), 진행 판정(`progress/`), `service_role` 사용이 전부 이 안에 있다.
- `CLAUDE.md` 3.2·3.3을 사람의 주의력이 아니라 **도구로 강제**한다.

Sprint 0에서는 폴더와 `supabase/`, `auth/`만 실제로 만들고, `grading/`·`progress/`는 자리만 둔다.

### 5.2 `features/` 를 미리 나눠 두는 이유

자유 배치·팀전·콘텐츠 공유를 **지금 구현하지는 않지만**, 나중에 이것들이 `app/` 안에 뒤섞여 들어가면 분리 비용이 커진다.

- 폴더와 한 줄 `README.md`만 만든다.
- **인터페이스나 추상 클래스를 미리 정의하지 않는다.** 요구가 확정되기 전의 추상화는 대개 틀린다.
- 개인전/팀전 분리(`CLAUDE.md` 4.2)는 `session/` 안에서 다루되, 구조는 Sprint 5에 결정한다.

### 5.3 `tests/` 를 프로젝트 루트에 두는 이유

이미 저장소에 `tests/` 폴더가 있고 `PROJECT.md` 문서 구조에도 기재돼 있다. 기존 구조를 따른다.

---

## 6. 환경 변수 목록

`.env.example`을 저장소에 커밋하고, 실제 값은 `.env.local`에만 둔다. **`.env.local`은 절대 커밋하지 않는다.**

### 6.1 Sprint 0에 필요한 변수

| 변수명 | 노출 | 용도 | 비고 |
| --- | --- | --- | --- |
| `NEXT_PUBLIC_SUPABASE_URL` | 공개 | Supabase 프로젝트 URL | 브라우저 노출 정상 |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | 공개 | 익명 키. RLS 적용 대상 | 브라우저 노출 정상. **RLS가 없으면 이 키로 전체 데이터가 열린다** |
| `SUPABASE_SERVICE_ROLE_KEY` | **비밀** | RLS 우회 서버 작업 | **`NEXT_PUBLIC_` 절대 금지.** `src/server/` 에서만 읽는다 |

> V-3 확인 결과에 따라 키 이름이 `publishable` / `secret` 계열로 바뀔 수 있다. 착수 시 실물을 확인하고 이 표를 갱신한다.

### 6.2 이후 스프린트에 추가될 변수 (지금은 만들지 않음)

| 변수명 | 시점 |
| --- | --- |
| `NEXT_PUBLIC_SITE_URL` | 인증 리디렉션 필요 시 (Sprint 1) |
| `DATABASE_URL` | 마이그레이션 도구 사용 시 (Sprint 1) |

### 6.3 안전 규칙

- `.env.local`이 `.gitignore`에 있는지 **커밋 전에 `git status`로 직접 확인**한다.
- `service_role` 키를 클라이언트 컴포넌트, `NEXT_PUBLIC_*`, 로그, 에러 메시지에 넣지 않는다.
- 키가 저장소에 한 번이라도 올라가면 **Supabase 대시보드에서 즉시 재발급**한다. 커밋을 지워도 이력에 남는다.
- 원격이 GitHub 공개 저장소인지 확인한다. 공개라면 유출 영향이 즉각적이다.

---

## 7. Git 브랜치 전략

1인 개발 + 3개월 MVP에 맞춘 최소 구성. GitFlow처럼 무거운 전략은 쓰지 않는다.

### 7.1 브랜치

| 브랜치 | 역할 |
| --- | --- |
| `main` | 항상 동작하는 상태. 직접 커밋하지 않는다 |
| `feat/*` | 기능 개발 |
| `fix/*` | 버그 수정 |
| `docs/*` | 문서만 변경 |
| `chore/*` | 설정·빌드·의존성 |

`develop` 브랜치는 두지 않는다. 1인 개발에서는 병합 부담만 늘고 얻는 것이 없다.

### 7.2 규칙

- **`main`에 직접 커밋하지 않는다.** 항상 브랜치 → PR → 병합.
  (예외: 오늘 만든 초기 커밋 `61beb51`은 저장소에 커밋이 없는 상태였으므로 예외로 둔다)
- 브랜치 하나는 **작업 하나**. 한 브랜치에 여러 기능을 섞지 않는다.
- 병합 전 확인: `npm run build`, `npm run lint`, `npm run test` 통과
- 병합 방식: **Squash merge**. 커밋 이력을 스프린트 단위로 읽기 쉽게 유지한다.
- 병합한 브랜치는 삭제한다.

### 7.3 커밋 메시지

Conventional Commits 형식을 쓴다.

```
<type>: <요약>

type — feat | fix | docs | chore | test | refactor
```

예: `chore: initialize Next.js with TypeScript and Tailwind`

### 7.4 Sprint 0 브랜치

```
chore/sprint-0-setup
```

Sprint 0 작업 전체를 이 브랜치에서 진행하고, 완료 후 PR로 `main`에 병합한다.

---

## 8. 완료 조건

아래를 **전부** 만족해야 Sprint 0을 종료한다. 하나라도 미충족이면 종료하지 않는다.

### 8.1 실행 검증

| # | 조건 | 확인 명령 |
| --- | --- | --- |
| C-1 | 개발 서버가 뜨고 첫 페이지가 열린다 | `npm run dev` |
| C-2 | 프로덕션 빌드가 성공한다 | `npm run build` |
| C-3 | 린트를 통과한다 | `npm run lint` |
| C-4 | 타입 오류가 없다 | `npx tsc --noEmit` |
| C-5 | Vitest 예시 테스트가 통과한다 | `npm run test` |
| C-6 | Playwright 예시 테스트가 통과한다 | `npm run test:e2e` |

> `CLAUDE.md` 5.2에 따라 **명령을 실제로 실행한 출력**으로 확인한다. 실행하지 못했으면 그대로 보고한다.

### 8.2 구조 검증

| # | 조건 |
| --- | --- |
| C-7 | §5의 폴더 구조가 만들어졌고, 각 폴더에 용도를 적은 `README.md`가 있다 |
| C-8 | `src/server/` 아래 파일에 `server-only`가 적용돼 있다 |
| C-9 | 클라이언트 컴포넌트에서 `src/server/`를 import하면 **빌드가 실패한다** (직접 시도해 확인) |
| C-10 | 규칙 상수가 `src/lib/constants/rules.ts` 한 곳에만 있다 |
| C-11 | `tsconfig.json`에 `strict: true`가 적용돼 있다 |

### 8.3 보안 검증

| # | 조건 |
| --- | --- |
| C-12 | `git status`에 `.env.local`이 나타나지 않는다 |
| C-13 | `SUPABASE_SERVICE_ROLE_KEY`가 `NEXT_PUBLIC_` 접두사를 쓰지 않는다 |
| C-14 | `.env.example`에 실제 키 값이 들어 있지 않다 |
| C-15 | 빌드 산출물(`.next/`)에서 `service_role` 키 문자열이 검색되지 않는다 |

### 8.4 문서 검증

| # | 조건 |
| --- | --- |
| C-16 | `README.md`의 "설치 및 실행" 섹션이 실제 명령으로 채워졌다 |
| C-17 | 이 문서에 V-1~V-7 확인 결과가 기록됐다 |
| C-18 | 확정한 의존성 버전이 기록됐다 |

### 8.5 Git 검증

| # | 조건 |
| --- | --- |
| C-19 | `chore/sprint-0-setup` 브랜치에서 작업했다 |
| C-20 | PR을 거쳐 `main`에 병합됐다 |

---

## 9. 위험 요소

| # | 위험 | 영향 | 발생 가능성 | 대응 |
| --- | --- | --- | --- | --- |
| R-1 | **네트워크 드라이브(Z:)에서 `npm install` 실패 또는 극심한 지연** | Sprint 0 전체 중단 | **높음** | Step 0에서 **가장 먼저** 검증. 실패 시 로컬 디스크로 이전을 즉시 논의. 이 판단을 미루면 하루를 통째로 날린다 |
| R-2 | **HMR(파일 감시) 미동작** | 개발 속도 심각한 저하 | 중간 | Step 0에서 함께 검증. 실패 시 폴링 감시 설정 또는 로컬 이전 |
| R-3 | **Tailwind v4 스캐폴딩으로 설정 방식이 다름** | 설정 시간 추가 | 중간 | V-2에서 확인. v4면 `tailwind.config` 대신 CSS 기반 설정을 따른다. 억지로 v3로 내리지 않는다 |
| R-4 | **Supabase 키 명칭 변경** | 문서와 실물 불일치 | 중간 | V-3에서 대시보드 실물 확인 후 문서 갱신 |
| R-5 | **`service_role` 키 실수 커밋** | **심각 — 전체 DB 노출** | 낮음 | C-12~C-15로 다중 확인. 발생 시 즉시 키 재발급. 커밋 삭제만으로는 해결되지 않음 |
| R-6 | Playwright 브라우저 다운로드 실패 (사내망·방화벽) | E2E 검증 지연 | 중간 | V-6에서 확인. 실패 시 Sprint 0에서는 Chromium 하나만 설치 |
| R-7 | `create-next-app`이 기존 `README.md` 덮어씀 | 문서 유실 | 중간 | Step 1에서 즉시 확인. Git에 커밋돼 있으므로 복원 가능 |
| R-8 | **선제 추상화 유혹** — 자유 배치·팀전 인터페이스를 미리 설계 | 잘못된 구조를 나중에 걷어내는 비용 | 중간 | §1.2 원칙 준수. 폴더와 한 줄 설명까지만 |
| R-9 | Node 24와 일부 패키지 호환성 경고 | 설치 경고, 드물게 실패 | 낮음 | V-7에서 확인. 문제 시 Node LTS 하위 버전 검토 |
| R-10 | Sprint 0 범위 확대 (인증·스키마까지 손댐) | 1~2일 일정 초과 | **중간** | §1.2 "하지 않을 것" 목록 준수. 완료 조건 충족 시 즉시 종료 |

### 9.1 가장 중요한 것

**R-1과 R-5** 두 가지다.

- **R-1**은 Sprint 0을 시작조차 못 하게 만든다. 그래서 Step 0의 첫 작업으로 배치했다.
- **R-5**는 되돌릴 수 없다. 나머지 위험은 시간이 더 들 뿐이지만, 이것은 프로젝트 전체의 데이터가 열린다.

---

## 10. Sprint 0 종료 시 생성되어야 할 파일 목록

### 10.1 설정 파일

| 파일 | 내용 |
| --- | --- |
| `package.json` | 의존성 + 스크립트 (`dev`, `build`, `lint`, `test`, `test:e2e`) |
| `package-lock.json` | 잠금 파일 |
| `tsconfig.json` | `strict: true`, `@/*` 별칭 |
| `next.config.ts` | Next.js 설정 |
| `eslint.config.mjs` | 린트 설정 |
| `postcss.config.mjs` | Tailwind용 |
| `tailwind.config.ts` | **Tailwind v3인 경우만.** v4면 CSS 기반 설정 |
| `vitest.config.ts` | `tests/unit/` 대상 |
| `playwright.config.ts` | `tests/e2e/` 대상, `webServer` 설정 |
| `.gitignore` | `node_modules/`, `.next/`, `.env*.local`, 테스트 산출물 |
| `.gitattributes` | `* text=auto eol=lf` |
| `.env.example` | 변수 이름만. **값 없음** |
| `.env.local` | 실제 값. **커밋하지 않음** |

### 10.2 애플리케이션 파일

| 파일 | 내용 |
| --- | --- |
| `src/app/layout.tsx` | 루트 레이아웃 (`lang="ko"`) |
| `src/app/page.tsx` | 임시 첫 페이지 |
| `src/app/globals.css` | Tailwind 진입점 |
| `src/lib/supabase/client.ts` | 브라우저 Supabase 클라이언트 |
| `src/server/supabase/server.ts` | 서버 Supabase 클라이언트 (`server-only`) |
| `src/lib/constants/rules.ts` | 규칙 상수 (Step 5의 8개) |

### 10.3 테스트 파일

| 파일 | 내용 |
| --- | --- |
| `tests/unit/rules.test.ts` | 상수 값 검증 예시 |
| `tests/e2e/smoke.spec.ts` | 첫 페이지 200 응답 확인 |

### 10.4 폴더 자리 (README.md 1줄 + .gitkeep)

| 폴더 | 용도 메모 |
| --- | --- |
| `src/app/(teacher)/` | 교사 화면 — Sprint 1~ |
| `src/app/(play)/` | 학생 플레이 — Sprint 3~ |
| `src/app/api/` | Route Handlers |
| `src/server/grading/` | 채점 (서버 전용) — Sprint 4~ |
| `src/server/progress/` | 진행 판정 (서버 전용) — Sprint 4~ |
| `src/server/auth/` | 권한 확인 |
| `src/features/builder/` | 제작기 (자유 배치) — Sprint 2~ |
| `src/features/play/` | 플레이 화면 — Sprint 3~ |
| `src/features/session/` | 세션·개인전·팀전 — Sprint 5~ |
| `src/features/library/` | 콘텐츠 공유 — Sprint 6~ |
| `src/components/ui/` | 공용 UI |
| `src/types/` | 공용 타입 |
| `src/lib/utils/` | 유틸 |
| `supabase/migrations/` | 스키마·RLS — Sprint 1~ |
| `supabase/seed/` | 마스터 데이터 |

### 10.5 갱신할 기존 파일

| 파일 | 변경 |
| --- | --- |
| `README.md` | "설치 및 실행" 7개 빈 섹션을 실제 명령으로 채움. "현재 개발 상태" 표에서 "Next.js 프로젝트 초기화"를 완료로 변경 |
| `docs/02_SPRINT_00_PLAN_REPLACED.md` | V-1~V-7 확인 결과, 확정 버전 기록 |

### 10.6 생성하지 않는 파일

혼동을 막기 위해 명시한다.

- 스키마 마이그레이션 (`supabase/migrations/*.sql`) — Sprint 1
- 인증 관련 페이지·미들웨어 — Sprint 1
- 채점 로직 구현 — Sprint 4
- 제작기 캔버스 컴포넌트 — Sprint 2
- CI 워크플로 (`.github/workflows/`) — 3개월차
- Vercel 설정 — 3개월차

---

## 11. 승인 요청

이 계획을 검토해 주세요. 특히 아래 3가지는 **승인 여부에 따라 진행이 달라집니다.**

| # | 확인이 필요한 사항 |
| --- | --- |
| 1 | **추가 의존성 5개** (§2.2) — 특히 `@supabase/ssr`과 `server-only`. `CLAUDE.md` 2.3에 따라 승인이 필요합니다 |
| 2 | **`src/` 디렉터리 사용** (§5) — 기존 `assets/`·`docs/`·`supabase/`와 앱 코드를 분리하는 구조입니다 |
| 3 | **Z: 드라이브 위험** (R-1) — 네트워크 드라이브에서 `npm install`이 실패하면 프로젝트 위치를 옮겨야 합니다. Step 0에서 먼저 검증하고 결과를 보고하겠습니다 |

승인해 주시면 Step 0(사전 확인)부터 시작하고, 각 단계 결과를 보고하겠습니다.
