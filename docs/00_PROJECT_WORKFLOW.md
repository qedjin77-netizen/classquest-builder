# Project Workflow

# 목적

이 문서는 ClassQuest Builder 프로젝트의 개발 규칙을 정의한다.

이 프로젝트에서는
항상 문서 중심(Document Driven Development)으로 개발한다.

---

# 역할

## Project Owner

사용자

역할

- 최종 의사결정
- 기능 승인
- 일정 승인
- 디자인 승인

---

## Project Architect

ChatGPT

역할

- 프로젝트 기획
- 시스템 설계
- 요구사항 정의
- 데이터 구조 설계
- UI/UX 설계
- 이미지 프롬프트
- Sprint 계획
- 품질 검토
- MVP 범위 관리

ChatGPT는
프로젝트 방향을 책임진다.

코드는 Claude Code가 작성한다.

---

## Lead Developer

Claude Code

역할

- 구현
- 테스트
- 리팩터링
- 버그 수정
- 성능 개선
- Git 관리
- Sprint 계획 문서 초안 작성 (방향은 Project Architect의 설계를 따르고, 확정은 Project Owner의 승인으로 한다)

Claude Code는 항상

- PROJECT.md
- CLAUDE.md
- tasks/NEXT_TASK.md
- docs/

를 먼저 읽고 작업한다.

---

# 개발 원칙

작업은 반드시 아래 순서를 따른다.

1. 문서를 읽는다.
2. 현재 Sprint를 확인한다.
3. 작업 계획을 작성한다.
4. 사용자의 승인을 받는다.
5. 구현한다.
6. 테스트한다.
7. 결과를 보고한다.
8. tasks/NEXT_TASK.md를 업데이트한다.
9. 현재 Sprint의 changelog/Sprint-NN.md를 업데이트한다.
10. Git Commit 메시지를 제안한다.

---

# 승인 없이 하면 안 되는 것

다음 작업은 사용자의 승인 없이 수행하지 않는다.

- 기술 스택 변경
- 라이브러리 추가
- DB 구조 변경
- API 구조 변경
- 폴더 구조 변경
- 대규모 리팩터링

---

# MVP 원칙

3개월 안에 반드시 완성한다.

AI 기능은 구현하지 않는다.

유료 콘텐츠 거래는 구현하지 않는다.

학생 30명이 안정적으로 사용할 수 있는 것이 최우선 목표이다.

## 데이터 계층 방침 — Supabase 연결 이연 (2026-08-03 결정)

Supabase 클라우드 프로젝트 생성, 실제 키 발급, 패키지 설치와 연결 작업은 UI와 기본 게임 흐름 구현 이후로 미룬다.

- Supabase 클라우드 프로젝트를 현재 생성하지 않는다.
- 실제 키를 현재 발급하거나 입력하지 않는다.
- Supabase 패키지와 연결 코드를 현재 추가하지 않는다.
- UI와 기본 게임 흐름은 mock data로 먼저 구현한다.
- 데이터 접근 계층은 나중에 Supabase로 교체하기 쉽도록 분리해 둔다.
- 교사 로그인, 실시간 학생 참여, 데이터 저장을 구현하기 직전에 Supabase를 연결한다.
- 정식 운영 전에 RLS, 권한 분리, 개인정보 보호, 백업, 요금제를 검토한다.

---

# Sprint 원칙

Sprint 하나는 하나의 목표만 가진다.

Sprint를 건너뛰지 않는다.

미완료 작업은 다음 Sprint로 넘긴다.

---

# 품질 원칙

코드는 읽기 쉬워야 한다.

작게 나눈다.

중복을 최소화한다.

TypeScript 타입을 적극 사용한다.

테스트 가능한 구조로 작성한다.

---

# Git

하나의 기능 = 하나의 Commit

Commit 메시지는 Conventional Commits 형식을 따른다.

예)

- feat:
- fix:
- refactor:
- docs:
- test:

---

# 문서 우선

문서와 코드가 다르면 문서를 우선한다.

문서가 잘못되었다고 판단되면 임의 수정하지 말고 사용자에게 먼저 질문한다.


---

---

# 문서 충돌 해결

문서 간 내용이 충돌하면 임의로 해석하거나 조용히 수정하지 않는다. 먼저 사용자에게 충돌과 영향을 보고한다.

판단 우선순위는 다음과 같다.

1. 사용자가 현재 작업에서 가장 최근에 명시적으로 승인한 결정
2. `PROJECT.md` — 현재 제품 사양과 범위
3. `docs/01_REQUIREMENTS_DECISIONS.md` — 확정 결정, 배경, 변경 이유
4. `CLAUDE.md` — 구현·보안·테스트 규칙
5. 승인된 현재 Sprint 계획
6. `docs/02_ARCHITECTURE.md` 및 관련 세부 설계 문서 (`docs/design/`, `docs/architecture/` 포함)
7. `README.md` — 소개와 탐색용 요약

충돌을 해소한 뒤에는 영향받는 문서를 함께 갱신한다. 파일이나 폴더 이름을 바꾸면 저장소 전체에서 이전 이름과 경로를 검색하고 모든 링크 및 일반 텍스트 참조를 동시에 수정한다.
