import { test, expect } from '@playwright/test';

test('noop requirement passes', () => {
  expect(true).toBe(true);
});
