# Current Sprint

Sprint 1

## Goal

프로젝트 개발 환경 구축

---

## TODO

- [ ] Next.js(App Router) 생성
- [ ] Tailwind CSS 설정
- [ ] ESLint 설정
- [ ] Prettier 설정
- [ ] Husky 설정
- [ ] lint-staged 설정
- [ ] Vitest 설정
- [ ] Playwright 설정
- [ ] Supabase 연결 준비
- [ ] 환경 변수(.env.example) 생성

---

## DONE

- [x] PROJECT.md 작성
- [x] README 작성
- [x] 요구사항 확정 (Sprint 0)
- [x] 워크플로우 문서 작성 (docs/00_PROJECT_WORKFLOW.md)
- [x] Sprint 1 계획 작성 (docs/sprints/Sprint-01-Setup-Plan.md, 승인 대기)


---

## Current Blocker

- **Z: 드라이브에서 node.exe 파일 쓰기 불가 (W-1 실패 확정, 2026-08-02).** `npm install`·`create-next-app`이 Z:에서 실행 불가. 로컬 디스크 이전 결정 전까지 Step 1 이후 진행 불가. 상세는 계획서 §1.4 참고.

## Decision Needed

- **프로젝트 작업 사본을 어느 로컬 경로로 이전할지** (예: `C:\dev\classquest-builder`). Z:의 원본은 git 원격(GitHub)과 함께 동기화 지점으로 유지 가능.

## Done Decisions

- `docs/sprints/Sprint-01-Setup-Plan.md` 승인 (2026-08-02)
- 추가 개발 의존성 A-1~A-7 승인 (2026-08-02)

## Risk

- 로컬 이전 후 Z: 원본과 로컬 사본의 이중 관리 — 동기화는 git(GitHub origin) 경유로만 한다.
- Next.js·Tailwind·Supabase 패키지의 최신 버전과 문서가 계획 작성 시점 이후 달라질 수 있으므로 설치 직전 실제 버전을 확인한다.
