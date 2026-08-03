import { expect, test } from "@playwright/test";

test("첫 페이지가 성공 응답으로 열린다", async ({ page }) => {
  const response = await page.goto("/");

  expect(response, "페이지 이동 응답이 있어야 한다").not.toBeNull();
  expect(response!.ok()).toBe(true);
});
