import { describe, expect, it } from "vitest";

import {
  MAX_QUESTIONS_PER_ROOM,
  MAX_STUDENTS_PER_SESSION,
  MAX_TEAM_COUNT,
  MIN_QUESTIONS_PER_ROOM,
  MIN_TEAM_COUNT,
  ROOM_COUNT,
} from "@/lib/constants/rules";

describe("게임 규칙 상수", () => {
  it("방은 3개다", () => {
    expect(ROOM_COUNT).toBe(3);
  });

  it("방당 문제 수의 하한은 상한보다 크지 않다", () => {
    expect(MIN_QUESTIONS_PER_ROOM).toBeLessThanOrEqual(MAX_QUESTIONS_PER_ROOM);
  });

  it("팀 수의 하한은 상한보다 크지 않다", () => {
    expect(MIN_TEAM_COUNT).toBeLessThanOrEqual(MAX_TEAM_COUNT);
  });

  it("세션 최대 학생 수는 30명이다", () => {
    expect(MAX_STUDENTS_PER_SESSION).toBe(30);
  });
});
