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

- 없음. 단, Z: 네트워크 드라이브에서 `npm install`과 파일 감시가 정상 동작하는지 Sprint 1 첫 단계에서 검증한다.

## Decision Needed

- `docs/sprints/Sprint-01-Setup-Plan.md` 승인
- 계획에 기재된 추가 개발 의존성 승인
- Z: 드라이브 검증 실패 시 프로젝트를 로컬 디스크로 이전할지 결정

## Risk

- 네트워크 드라이브에서 패키지 설치·HMR·파일 잠금이 불안정할 수 있다.
- Next.js·Tailwind·Supabase 패키지의 최신 버전과 문서가 계획 작성 시점 이후 달라질 수 있으므로 설치 직전 실제 버전을 확인한다.
