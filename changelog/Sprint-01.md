# Sprint 01 Change Log

## Sprint 정보

- 목표: 프로젝트 개발 환경 구축
- 상태: **완료 (2026-08-03)** — Step 0(검증)·1(스캐폴딩)·2(설정 고정)·3(Husky·lint-staged)·4(폴더 골격)·6(규칙 상수)·7(테스트 환경)·8(최종 검증·README·PR) 완료. Step 5(Supabase 연결)는 이연 유지 (2026-08-03 결정, 계획서 §12). **다음 작업: Sprint 2 계획 수립 및 승인**
- 계획: [../docs/sprints/Sprint-01-Setup-Plan.md](../docs/sprints/Sprint-01-Setup-Plan.md)

## Added

- 2026-08-03 — Step 8: 최종 검증·README 정리·PR 생성. README.md의 낡은 상태 문구("초기 설정(문서화)", "애플리케이션 코드 없음")를 현재 상태로 교정하고 "설치 및 실행"을 실제 명령으로 작성(요구 환경 Node 24·npm, install/dev/build/start/lint/tsc/format/test/test:watch/test:e2e, 환경 변수 안내 — Supabase 이연으로 `.env.local` 불필요 명시, DB·배포는 이후 단계 표시). 전체 검증 결과와 PR은 아래 Verification 참조.
- 2026-08-03 — Step 7: 테스트 환경 구축. devDependencies 설치(승인 A-3·A-4 범위): vitest 4.1.10, @vitejs/plugin-react 6.0.5, vite-tsconfig-paths 6.1.1, @playwright/test 1.62.1 (모두 Node v24 호환 확인). 생성: `vitest.config.ts`(tests/unit 대상, `@/` 별칭 해석), `tests/unit/rules.test.ts`(규칙 상수 4개 검증), `playwright.config.ts`(tests/e2e 대상, Chromium 단일, webServer로 dev 서버 자동 기동), `tests/e2e/smoke.spec.ts`(첫 페이지 성공 응답 — 문구·디자인 비의존). package.json에 test·test:watch·test:e2e 스크립트 추가, tests README 2개 실명령 기준으로 갱신. 결과: **Vitest 4/4 통과(1.09s), Playwright 1/1 통과(23.9s, Chromium 설치 성공)**. Supabase 패키지·연결 없음.
- 2026-08-03 — Step 6: 규칙 상수 `src/lib/constants/rules.ts` 생성. named export 숫자 상수 8개 (계획서 §2.4와 일치): `ROOM_COUNT=3` `MIN_QUESTIONS_PER_ROOM=3` `MAX_QUESTIONS_PER_ROOM=5` `HINT_UNLOCK_WRONG_COUNT=2` `HINTS_PER_QUESTION=1` `MIN_TEAM_COUNT=2` `MAX_TEAM_COUNT=6` `MAX_STUDENTS_PER_SESSION=30`. 함수·객체·enum 없음, 팀 정원·문제 유형·과목·학년 상수 없음, 화면·실행 코드 연결 없음. 검증: 실행 코드 내 규칙값 중복 정의 없음 확인, `npm run lint`·`npx tsc --noEmit`·`npm run format:check`·`npm run build` 통과 (결과는 커밋 기록 참조).
- 2026-08-02 — Step 2: 설정 고정. `.gitattributes`(LF 기준·바이너리 지정), `.env.example`(변수 이름만: NEXT_PUBLIC_SUPABASE_URL·NEXT_PUBLIC_SUPABASE_ANON_KEY·SUPABASE_SERVICE_ROLE_KEY), `.prettierrc`(tailwind 플러그인), `.prettierignore`(md 문서·산출물·자산 제외). `.gitignore` 보완(test-results·playwright-report 추가, `!.env.example` 예외). `eslint.config.mjs`에 eslint-config-prettier 적용. package.json에 format·format:check 스크립트 추가. devDependencies 추가: prettier 3.9.6, prettier-plugin-tailwindcss 0.8.1, eslint-config-prettier 10.1.8 (승인 A-6·A-7). `.env.local`은 실제 값이 없어 미생성(Supabase 연결 시점에 작성 — 이후 이연 결정).
- 2026-08-02 — Step 1: Next.js 16.2.12 스캐폴딩 (`chore/sprint-1-setup` 브랜치). TypeScript·Tailwind v4·ESLint·App Router·`src/` 디렉터리·`@/*` 별칭·Turbopack. 생성 파일: `package.json`(이름 classquest-builder로 정정), `tsconfig.json`, `next.config.ts`, `eslint.config.mjs`, `postcss.config.mjs`, `.gitignore`, `src/app/*`, `public/` 기본 에셋. 저장소에 기존 문서가 많아 임시 폴더에 생성 후 이식(제외: 스캐폴드의 README.md·CLAUDE.md·AGENTS.md — 기존 프로젝트 문서 보존).

## Changed

아직 구현 작업 없음.

## Fixed

- 2026-08-02 — docs/sprints/Sprint-01-Setup-Plan.md: 문서 끝의 "구현 체크리스트" 중복 2건을 1건으로 병합하고, "승인 요청"과 겹치던 절 번호를 10 → 11로 정정.
- 2026-08-02 — 루트의 구버전 NEXT_TASK.md·CHANGELOG.md 정리 (문서 구조 개편 시 tasks/NEXT_TASK.md·changelog/로 이전 완료된 파일의 잔재. 구경로 참조를 포함하고 있어 현행 문서와 불일치). 구내용을 현행 위치 안내 스텁으로 교체했으며 파일 자체는 삭제 예정.

## Decisions

- 패키지 매니저는 npm을 사용한다.
- Sprint 1에서는 게임 기능을 구현하지 않는다.
- ~~Supabase는 우선 클라우드 프로젝트 연결 방식으로 준비한다.~~ → 2026-08-03 아래 결정으로 대체.
- **2026-08-03 — Supabase 연결 이연 (Project Owner 결정):** Supabase 클라우드 프로젝트 생성·실제 키 발급·패키지 설치·연결 코드를 지금 하지 않고 **UI와 기본 게임 흐름 구현 이후로 연기**한다. 원칙: ① 클라우드 프로젝트 미생성 ② 실제 키 미발급·미입력 ③ Supabase 패키지·연결 코드 미추가 ④ UI·기본 게임 흐름은 mock data로 선구현 ⑤ 데이터 접근 계층은 Supabase로 교체하기 쉽게 분리 ⑥ 교사 로그인·실시간 학생 참여·데이터 저장 구현 직전에 연결 ⑦ 정식 운영 전 RLS·권한 분리·개인정보 보호·백업·요금제 검토. Sprint 1 진행 순서는 Step 4 → 6 → 7 → 8로 조정. Supabase 폴더 골격과 `.env.example` 변수 이름은 유지(값 없음). C-9 검증은 연결 시점으로 이연. (계획서 §12, docs/00_PROJECT_WORKFLOW.md 데이터 계층 방침에 기록)

## Verification

### 2026-08-02 — Step 0: 개발 환경·Z: 드라이브 검증

- 도구 버전 확인: Node v24.15.0, npm 11.12.1, Git 2.54.0 — 계획서 기록과 일치.
- W-3 (`safe.directory`): 전역 등록 완료. git status/commit/push 정상 동작 확인.
- W-1 (Z:에서 npm 설치): **실패 확정.** Z: 임시 폴더에서 `npm init`·`npm install`이 EPERM으로 실패. node.exe의 파일 생성·쓰기·rename이 Z:에서 전부 거부됨(진단 스크립트로 확인). 동일 시험이 로컬 C:에서는 모두 성공(npm install 포함) → Z: 드라이브 고유 문제로 판정. git.exe·PowerShell의 쓰기는 정상.
- W-2 (파일 감시): 미검증 — W-1 실패로 Z: 개발이 불가하여 로컬 이전 후 확인.
- 결론: 계획 §9 R-1 발생. **로컬 디스크 이전 결정 대기** (tasks/NEXT_TASK.md Blocker 기재).

### 2026-08-02 — R-1 대응: 로컬 디스크 이전 완료

- 추가 진단: Z:·X:·Y:는 문서중앙화 솔루션 가상 드라이브(NPFS, PlusDrive 에이전트), O:/P: 보안디스크는 node 읽기 차단 → 로컬 C:만 개발 가능 판정. robocopy도 Z: 읽기가 차단되어 PowerShell Copy-Item + GitHub clone 방식으로 이전.
- 프로젝트 폴더 전체를 `C:\Users\user\Documents\WM 게임 프로젝트\4. 게임, 퀴즈 프로젝트`로 이전. 저장소는 GitHub에서 clone(`0a31c4c`, origin과 동기화), 저장소 외 파일 54개는 Copy-Item으로 복사(개수 일치 확인).
- 새 경로(한글·공백 포함)에서 `npm init`·`npm install`·`require` 정상 동작 확인.
- 이후 개발 작업 위치는 로컬 사본이며, Z:와의 공유는 git 원격(GitHub) 경유로만 한다.

### 2026-08-02 — Step 1: 스캐폴딩 검증

- `npm install` 106초, peer 경고 없음 (V-7).
- `npm run dev` 기동 → `http://localhost:3000` HTTP 200 응답 확인.
- W-2 (파일 감시): dev 서버 기동 중 `page.tsx` 수정 → 153ms에 재컴파일 확인. **통과.** 시험용 수정은 되돌림.
- 버전 실물 확인: Next 16.2.12, Tailwind 4.3.3(v4, CSS 기반), React 19.2.4, TS 5.9.3 — 계획서 §3.4 결과표에 기록.

### 2026-08-02 — Step 2: 설정 고정 검증

- `npm run lint` 통과 (Prettier 정리 후 재실행도 통과).
- `npx tsc --noEmit` 오류 없음.
- `npm run format:check` — 최초 실행에서 스캐폴드 3개 파일 지적 → `npm run format` 후 "All matched files use Prettier code style!" 통과.
- `.env.example` — `!.env.example` 규칙으로 추적 대상 확인, 커밋 `c18c2c8`에 포함됨. 내용은 변수 이름 3개뿐(값 없음).
- `.env.local` — `.env*` 규칙으로 미추적 확인 (`git check-ignore`). 실제 값이 없어 파일 자체를 만들지 않음.
- 비밀값 스캔 — 저장소 내 실제 키 문자열 없음 (package-lock의 sha512 무결성 해시만 검출, 비밀 아님).
- `npm audit`: high 3건(`sharp` 전이 의존성). 제안된 자동 수정이 Next 9 다운그레이드라 미적용, Step 8에서 재확인.

### 2026-08-02 — Step 3: Husky·lint-staged 실동작 시험

- husky 9.1.7, lint-staged 17.3.0 설치 (Node v24.15.0 호환 확인: husky ≥18, lint-staged ≥22.22.1).
- `.husky/pre-commit` = `npx lint-staged`. `prepare: husky` 스크립트 추가.
- **통과 시험**: 정상 TS 파일 stage → pre-commit에서 eslint·prettier 실행 로그 확인 → 커밋 성공. 시험 커밋은 `git reset HEAD~1`로 제거.
- **차단 시험**: 구문 오류 TS 파일 stage → eslint 파싱 오류로 훅 실패(`husky - pre-commit script failed (code 1)`) → **커밋 차단 확인**, HEAD 불변. 시험 파일 제거.
- V-8(pre-commit 실동작): **통과** — 로컬 경로 기준.

### 2026-08-03 — Step 8: Sprint 1 최종 검증

- 실행 명령별 결과 (모두 통과): `npm run dev` 첫 페이지 HTTP 200 후 종료 · `npm run lint` exit 0 · `npx tsc --noEmit` exit 0 · `npm run format:check` 통과 · `npm run test` **Vitest 4/4 통과** · `npm run test:e2e` **Playwright 1/1 통과(Chromium)** · `npm run build` exit 0.
- `npm audit`: **high 3건 — `sharp` (직접 의존성 아님, `next`의 전이 의존성).** 제안된 자동 수정(`npm audit fix --force`)이 `next@9.3.3`으로의 메이저 다운그레이드라 **적용하지 않음.** 패키지 버전 임의 변경 없음. Next 패치 릴리스에서 해소 여부를 추후 확인한다.
- 구조·보안 검증 (모두 통과): 폴더 골격 20개+README 유지 · rules.ts 상수 8개 정확 · 실행 코드 내 규칙값 중복 정의 없음 · TypeScript strict 활성 · `.env.example` 추적됨 · `.env.local`·`.env*` 미추적 · 추적 파일 내 비밀값 없음(스캔) · `NEXT_PUBLIC_` 접두사 서버 키 없음 · `.next`/`node_modules`/`coverage`/`test-results`/`playwright-report` 미추적 · Supabase 패키지·연결 코드 없음 · 테스트 후 dev 서버·Playwright·Chromium 잔류 프로세스 없음(포트 3000의 TimeWait 소켓 잔상만 확인됨, 라이브 서버 아님).
- 최종 설치 버전: Next.js 16.2.12 · React 19.2.4 · TypeScript 5.9.3 · Tailwind 4.3.3 · Vitest 4.1.10 · @vitejs/plugin-react 6.0.5 · vite-tsconfig-paths 6.1.1 · @playwright/test 1.62.1 · Prettier 3.9.6 · prettier-plugin-tailwindcss 0.8.1 · eslint-config-prettier 10.1.8 · Husky 9.1.7 · lint-staged 17.3.0.
- 미완료(의도적): Step 5 Supabase 연결 — 이연 결정 유지. C-9(server-only 빌드 실패 검증)도 연결 시점으로 이연.
- Step 3 종료 시 최종 검사 (모두 통과): `npm run lint` exit 0 · `npx tsc --noEmit` exit 0 · `npm run format:check` "All matched files use Prettier code style!" · `npm run build` exit 0 (정적 라우트 `/`·`/_not-found` 생성) · 최종 `git status`: 커밋 `b751bb4` push 후 working tree clean, origin과 동기화.

### 2026-08-03 — Step 4: 폴더 골격 생성·검증

- 계획서 §4·§2.5의 폴더 20개 생성, 각 폴더에 용도 한 줄 README.md 추가:
  `src/app/(teacher)` `src/app/(play)` `src/app/api` / `src/server/{supabase,grading,progress,auth}` / `src/features/{builder,play,session,library}` / `src/lib/{constants,supabase,utils}` / `src/components/ui` `src/types` / `supabase/{migrations,seed}` / `tests/{unit,e2e}`
- 구현 코드·인터페이스·라우트·스키마·상수 파일은 만들지 않음 (선제 추상화 금지 준수). `server-only`·Supabase 패키지 미설치 (이후 2026-08-03 결정으로 Supabase 연결 자체가 이연됨 — 계획서 §12).
- 기존 `src/app` 라우트 파일·프로젝트 문서·assets·public 무변경.
- 검증 (모두 통과): 폴더 20개·README 20개 존재 확인, 실행 코드 미추가 확인(git 변경분이 README 20개 + 문서 교정뿐), `npm run lint`·`npx tsc --noEmit`·`npm run format:check`·`npm run build` 통과.
