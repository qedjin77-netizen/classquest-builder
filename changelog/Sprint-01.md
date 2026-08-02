# Sprint 01 Change Log

## Sprint 정보

- 목표: 프로젝트 개발 환경 구축
- 상태: 진행 중 — 계획 및 추가 의존성 A-1~A-7 승인됨 (2026-08-02), Step 0 검증 완료
- 계획: [../docs/sprints/Sprint-01-Setup-Plan.md](../docs/sprints/Sprint-01-Setup-Plan.md)

## Added

- 2026-08-02 — Step 2: 설정 고정. `.gitattributes`(LF 기준·바이너리 지정), `.env.example`(변수 이름만: NEXT_PUBLIC_SUPABASE_URL·NEXT_PUBLIC_SUPABASE_ANON_KEY·SUPABASE_SERVICE_ROLE_KEY), `.prettierrc`(tailwind 플러그인), `.prettierignore`(md 문서·산출물·자산 제외). `.gitignore` 보완(test-results·playwright-report 추가, `!.env.example` 예외). `eslint.config.mjs`에 eslint-config-prettier 적용. package.json에 format·format:check 스크립트 추가. devDependencies 추가: prettier 3.9.6, prettier-plugin-tailwindcss 0.8.1, eslint-config-prettier 10.1.8 (승인 A-6·A-7). `.env.local`은 실제 값이 없어 미생성(Step 5에서 작성).
- 2026-08-02 — Step 1: Next.js 16.2.12 스캐폴딩 (`chore/sprint-1-setup` 브랜치). TypeScript·Tailwind v4·ESLint·App Router·`src/` 디렉터리·`@/*` 별칭·Turbopack. 생성 파일: `package.json`(이름 classquest-builder로 정정), `tsconfig.json`, `next.config.ts`, `eslint.config.mjs`, `postcss.config.mjs`, `.gitignore`, `src/app/*`, `public/` 기본 에셋. 저장소에 기존 문서가 많아 임시 폴더에 생성 후 이식(제외: 스캐폴드의 README.md·CLAUDE.md·AGENTS.md — 기존 프로젝트 문서 보존).

## Changed

아직 구현 작업 없음.

## Fixed

- 2026-08-02 — docs/sprints/Sprint-01-Setup-Plan.md: 문서 끝의 "구현 체크리스트" 중복 2건을 1건으로 병합하고, "승인 요청"과 겹치던 절 번호를 10 → 11로 정정.
- 2026-08-02 — 루트의 구버전 NEXT_TASK.md·CHANGELOG.md 정리 (문서 구조 개편 시 tasks/NEXT_TASK.md·changelog/로 이전 완료된 파일의 잔재. 구경로 참조를 포함하고 있어 현행 문서와 불일치). 구내용을 현행 위치 안내 스텁으로 교체했으며 파일 자체는 삭제 예정.

## Decisions

- 패키지 매니저는 npm을 사용한다.
- Sprint 1에서는 게임 기능을 구현하지 않는다.
- Supabase는 우선 클라우드 프로젝트 연결 방식으로 준비한다.

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
