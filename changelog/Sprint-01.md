# Sprint 01 Change Log

## Sprint 정보

- 목표: 프로젝트 개발 환경 구축
- 상태: 진행 중 — 계획 및 추가 의존성 A-1~A-7 승인됨 (2026-08-02), Step 0 검증 완료
- 계획: [../docs/sprints/Sprint-01-Setup-Plan.md](../docs/sprints/Sprint-01-Setup-Plan.md)

## Added

아직 구현 작업 없음.

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
