# ADR-001 — Supabase 사용

- 상태: 승인됨
- 날짜: 2026-08-02

## 결정

백엔드, PostgreSQL 데이터베이스, 인증, RLS, Realtime에 Supabase를 사용한다.

## 이유

- 교사 1명과 학생 최대 30명의 실시간 세션을 빠르게 구축할 수 있다.
- PostgreSQL과 RLS로 교사·학생 데이터 접근을 명시적으로 제한할 수 있다.
- Next.js와의 연동 및 Vercel 배포 흐름이 단순하다.

## 결과

- 모든 신규 테이블에 RLS를 적용한다.
- service role 키를 클라이언트에 노출하지 않는다.
- 실시간 기능은 Supabase Realtime을 우선 사용한다.
