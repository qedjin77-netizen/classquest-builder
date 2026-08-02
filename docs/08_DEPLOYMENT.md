# Deployment Guide

## 목표 환경

- 애플리케이션: Vercel
- 백엔드·DB·Realtime: Supabase
- 소스 관리: GitHub

## 환경 구분

- local
- preview/staging
- production

환경별 Supabase 프로젝트 또는 안전한 분리 정책을 사용한다. production 비밀값을 로컬 예시 파일에 기록하지 않는다.

## 필수 배포 점검

- `npm run lint` 통과
- 단위·통합 테스트 통과
- Playwright 핵심 흐름 통과
- `npm run build` 통과
- 환경 변수 누락 없음
- service role 키 클라이언트 노출 없음
- RLS 적용 확인
- 학생 30명 동시 접속 부하 테스트
- 오디오 실패 시 게임 진행 가능 확인
- 게시 버전과 진행 중 세션 버전 고정 확인

## 롤백

- Vercel 이전 배포로 롤백 가능해야 한다.
- DB 마이그레이션은 되돌리기 계획을 포함한다.
- 게시된 콘텐츠 스냅샷을 마이그레이션으로 임의 변경하지 않는다.
