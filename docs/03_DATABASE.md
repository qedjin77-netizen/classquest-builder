# Database Design Guide

이 문서는 DB 구현 전 기준을 정의한다. 실제 컬럼·인덱스·정책은 별도 스키마 승인 후 확정한다.

## 핵심 영역

1. 교사와 소유권
2. 게임 초안과 게시 버전
3. 방·오브젝트·문제·정답·힌트·오디오
4. 수업 세션과 학생 세션
5. 개인전·팀전 진행 상태
6. 시도·힌트 해제·도움 요청·교사 확인 완료
7. 공개 콘텐츠와 복제 관계

## 필수 원칙

- 모든 테이블에 RLS 적용
- 정답과 잠긴 힌트는 학생 직접 접근 금지
- 게시 버전은 불변 스냅샷
- `studentSessionId` 기반 식별
- 개인전과 팀전 진행 테이블 분리
- `teacher_overrides`와 정답 시도 기록 분리
- 과목·학년·자산은 마스터 데이터로 관리

## 초기 테이블 후보

- `profiles`
- `games`, `game_drafts`, `game_versions`
- `rooms`, `placed_objects`, `questions`, `question_answers`
- `asset_catalog`
- `class_sessions`, `student_sessions`, `teams`, `team_members`
- `player_progress`, `team_progress`
- `attempts`, `hint_unlocks`, `help_requests`, `teacher_overrides`

> 테이블명과 관계는 Sprint별 DB 설계 승인을 받은 뒤 마이그레이션으로 확정한다.
