import { test, expect } from '@playwright/test'

test('orangehrm homepage opens', async ({ page }) => {
  await page.goto('https://orangehrm.lan.home')

  await expect(page).toHaveURL(/orangehrm/)

  await expect(page).toHaveTitle(/OrangeHRM/)
})