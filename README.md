# ClassQuest Builder

교실용 방탈출 학습 게임 제작 및 플레이 플랫폼.

교사가 코딩 없이 자기 수업 내용으로 방탈출 게임을 만들고, 학생들이 같은 교실에서 함께 플레이한다.

- **대상**: 한국 초등학교 3~6학년
- **규모**: 교사 1명 + 학생 최대 30명
- **구성**: 방 3개, 방마다 필수 문제 3~5개
- **목표**: 3개월 MVP

---

## 핵심 기능

### 교사용 게임 제작기

- 방 배경 위에 오브젝트를 **자유롭게 드래그 배치** (격자 스냅 없음)
- 이동 · 크기 조절 · 회전 · 복사 · 삭제 · 잠금 · 레이어 · **Undo / Redo**
- 오브젝트에 문제 연결 (객관식, 복수 정답, 단답형, OX)
- **자동 저장은 초안에만** 적용 — 게시하면 **불변 스냅샷 버전**이 생성된다
- 게시된 버전은 수정하지 않는다. 고치려면 초안을 편집해 **새 버전으로 다시 게시**한다
- 게시 전 자동 검증 (방 3개, 방당 문제 3~5개, 오브젝트 연결, 정답·힌트 누락 확인)
- 배경·오브젝트·오디오는 **제공 자산 라이브러리**에서 선택 (MVP에는 교사 업로드 없음)

### 학생 플레이

- 세션 코드 + 닉네임으로 **회원가입 없이** 참여 (닉네임 중복 허용)
- 방 안의 문제 오브젝트를 **원하는 순서로 자유 탐색**
- **무제한 오답 재도전** — 틀려도 계속 다시 풀 수 있다
- **같은 문제를 2회 틀리면 힌트** 공개 (문제당 힌트 1개)
- 현재 방의 **문제를 모두 맞히면 다음 방 출구가 열린다** (1번 방 → 2번 방 → 3번 방 순차)
- 방 3개를 모두 통과하면 탈출
- 계속 막히면 **"교사에게 도움 요청"** 버튼으로 교사를 부른다

### 세션 운영

- **개인전**과 **기본 팀전** 지원 (진행 데이터는 서로 분리해 관리)
- 팀전은 교사가 **2~6팀**을 고르고 학생을 **균등 배정**한다
  - 팀원 1명이 풀면 **팀의 해당 문제는 해결 완료**
  - **오답과 힌트는 개인별** — 팀원에게 힌트를 자동 공유하지 않는다
- **세션 시간 제한**은 선택 기능이며 기본값은 제한 없음
- **재접속** — 브라우저를 닫아도 진행 상태가 복구된다
- **실시간 진행 확인** — 교사 대시보드에서 학생별 현재 방, 푼 문제 수, 오답이 많은 문제, 도움 요청을 실시간 확인
- 막힌 학생의 특정 문제를 **"교사 확인 완료"**로 처리할 수 있다 (정답 기록과 구분해 저장)

### 콘텐츠 공유

- 만든 게임을 **공개**하고, 과목·학년·키워드로 **검색**
- **미리보기**로 확인한 뒤 **복제**해서 자기 수업에 맞게 수정 (복제본은 새 초안)
- 미리보기도 학생 플레이와 **동일한 서버 판정 방식**을 쓴다 — 정답이 노출되지 않는다
- **유료 콘텐츠 거래는 제외** — 무료 공개·검색·미리보기·복제만 지원한다

### 오디오

- **대기실 전용 BGM**과 효과음
- **방마다 서로 다른 BGM과 환경음**
- **탈출 화면 전용 BGM**과 효과음
- 전체 음소거 / BGM만 음소거 지원
- 파일은 **관리자·개발자가 등록한 자산**에서만 선택한다

### 지원 과목

국어 · 수학 · 사회 · 과학 · 영어 · 도덕 (3~6학년), 실과 (5~6학년)

### 만들지 않는 것 (MVP 제외)

- **AI 기능 전체** — 문제 자동 생성, 자동 채점 보조, 힌트 생성, 챗봇, 추천 등 모든 AI/LLM 연동을 제외한다
- **유료 콘텐츠 거래** — 결제, 마켓플레이스 판매, 구독
- **선택 문제·보너스 문제** — 모든 문제가 필수다
- **교사의 강제 다음 방 이동** — 진행 보조는 "교사 확인 완료"로만 한다
- **교사의 이미지·오디오 업로드** — 제공 자산에서만 선택한다
- **다단계 힌트** — 문제당 힌트는 1개다

전체 목록과 결정 배경은 [docs/01_REQUIREMENTS_DECISIONS.md](docs/01_REQUIREMENTS_DECISIONS.md)에 있다.

---

## 기술 스택

| 영역 | 기술 |
| --- | --- |
| 프레임워크 | Next.js (App Router) |
| UI | React |
| 언어 | TypeScript |
| 스타일링 | Tailwind CSS |
| 백엔드 · 인증 | Supabase |
| 데이터베이스 | PostgreSQL |
| 실시간 통신 | Supabase Realtime |
| 배포 | Vercel |
| 단위 · 통합 테스트 | Vitest |
| E2E 테스트 | Playwright |

### 보안 원칙

- 정답 원문을 **브라우저 번들·HTML·클라이언트 상태에 포함하지 않는다**
- 정답 판정은 **서버에서만** 한다 (미리보기도 동일)
- 정답은 **교사용 문제 편집 화면에서만** 권한 확인 후 조회할 수 있다
- 모든 테이블에 **Supabase RLS**를 적용한다
- 게시된 게임 버전은 **불변**이다

---

## 현재 개발 상태

**단계: 프로젝트 셋업 완료 (Sprint 1, 2026-08-03)** — 게임 기능 구현은 아직 시작하지 않았다.

| 항목 | 상태 |
| --- | --- |
| 프로젝트 문서 (`PROJECT.md`, `CLAUDE.md`, `README.md`) | 완료 |
| 요구사항 결정 기록 (`docs/01_REQUIREMENTS_DECISIONS.md`) | 완료 (2026-08-02 확정) |
| 시스템 아키텍처 초안 (`docs/02_ARCHITECTURE.md`) | 완료 |
| Next.js 프로젝트 초기화 | **완료** — Next.js 16.2.12, TypeScript strict, Tailwind v4, App Router |
| 코드 품질 도구 | **완료** — ESLint + Prettier, Husky pre-commit(lint-staged) |
| 테스트 환경 | **완료** — Vitest(단위) + Playwright(E2E, Chromium) 예시 테스트 통과 |
| 폴더 골격 + 규칙 상수 | **완료** — `src/lib/constants/rules.ts` |
| Supabase 연결 | **이연** — UI·기본 게임 흐름을 mock data로 구현한 이후 연결 (2026-08-03 결정, `docs/00_PROJECT_WORKFLOW.md` 데이터 계층 방침) |
| Supabase 스키마 · RLS | 예정 (Supabase 연결 이후) |
| 교사용 제작기 | 예정 |
| 학생 플레이 화면 | 예정 |
| 실시간 대시보드 | 예정 |
| 오디오 | 예정 |
| 콘텐츠 공유 | 예정 |

상세 일정은 [PROJECT.md](PROJECT.md)의 "3개월 MVP 일정"을 참고한다.

---

## 문서 구조

```text
classquest-builder/
├─ PROJECT.md                 프로젝트 전체 사양
├─ CLAUDE.md                  Claude Code 개발 규칙
├─ README.md                  프로젝트 소개와 문서 안내
│
├─ tasks/
│  ├─ NEXT_TASK.md            현재 Sprint의 작업
│  ├─ BACKLOG.md              후순위·승인 대기 작업
│  └─ DONE.md                 완료 작업 요약
│
├─ changelog/
│  ├─ README.md               Sprint 변경 이력 목차
│  ├─ Sprint-00.md            요구사항 확정 이력
│  └─ Sprint-01.md            프로젝트 셋업 이력
│
├─ decisions/
│  ├─ README.md               ADR 목차
│  ├─ ADR-001-SUPABASE.md
│  ├─ ADR-002-TEAM-MODE.md
│  ├─ ADR-003-VERSION-POLICY.md
│  └─ ADR-004-STUDENT-IDENTITY.md
│
├─ docs/
│  ├─ 00_PROJECT_WORKFLOW.md
│  ├─ 01_REQUIREMENTS_DECISIONS.md
│  ├─ 02_ARCHITECTURE.md
│  ├─ 03_DATABASE.md
│  ├─ 04_UI_GUIDE.md
│  ├─ 05_ART_GUIDE.md
│  ├─ 06_AUDIO_GUIDE.md
│  ├─ 07_GAME_RULE.md
│  ├─ 08_DEPLOYMENT.md
│  ├─ sprints/
│  │  └─ Sprint-01-Setup-Plan.md
│  └─ archive/
│     └─ 02_SPRINT_00_PLAN_REPLACED.md
│
├─ assets/
├─ public/
├─ src/
├─ supabase/
└─ tests/
```

### 읽는 순서

1. [README.md](README.md) — 프로젝트 개요
2. [docs/00_PROJECT_WORKFLOW.md](docs/00_PROJECT_WORKFLOW.md) — 협업·승인 절차
3. [PROJECT.md](PROJECT.md) — 제품 사양
4. [docs/01_REQUIREMENTS_DECISIONS.md](docs/01_REQUIREMENTS_DECISIONS.md) — 결정 배경
5. [CLAUDE.md](CLAUDE.md) — 구현 규칙
6. [docs/02_ARCHITECTURE.md](docs/02_ARCHITECTURE.md) — 시스템 구조
7. [tasks/NEXT_TASK.md](tasks/NEXT_TASK.md) — 현재 실행할 작업

> 사양은 `PROJECT.md`, 결정 이유는 `docs/01_REQUIREMENTS_DECISIONS.md`, 구현 규칙은 `CLAUDE.md`를 기준으로 한다.

## 설치 및 실행

### 요구 환경

- Node.js 24 (개발 기준: v24.15.0)
- npm (패키지 매니저는 npm으로 고정)

### 설치

```bash
npm install
```

주요 설치 버전: Next.js 16.2.12 · React 19.2.4 · TypeScript 5.9.3 · Tailwind CSS 4.3.3 · Vitest 4.1.10 · Playwright 1.62.1 · Prettier 3.9.6 · ESLint 9 · Husky 9.1.7 · lint-staged 17.3.0

### 개발 서버 실행

```bash
npm run dev
```

`http://localhost:3000`에서 열린다.

### 프로덕션 빌드

```bash
npm run build
npm run start
```

### 코드 검사

```bash
npm run lint
npx tsc --noEmit
npm run format:check
```

커밋 시 Husky pre-commit 훅이 staged 파일에 ESLint·Prettier를 자동 실행한다.

### 단위 테스트 (Vitest)

```bash
npm run test
npm run test:watch
```

### E2E 테스트 (Playwright)

최초 1회 Chromium을 설치한 뒤 실행한다. dev 서버는 자동 기동된다.

```bash
npx playwright install chromium
npm run test:e2e
```

### 환경 변수

- `.env.example`에는 **변수 이름만** 있다 (값 없음).
- **Supabase 연결이 이연되어 현재는 `.env.local`이 필요하지 않다.**
- 실제 연결 시점에 `.env.local`에 값을 넣어 사용하며, 이 파일은 Git에 올리지 않는다. `SUPABASE_SERVICE_ROLE_KEY`는 서버 전용이며 `NEXT_PUBLIC_` 접두사를 절대 붙이지 않는다.

### 데이터베이스 설정

_(이후 단계 — Supabase 연결 시점에 마이그레이션·시드 절차를 작성한다.)_

### 배포

_(이후 단계 — Vercel. 3개월차에 진행한다.)_

---

## 라이선스

_(미정)_
