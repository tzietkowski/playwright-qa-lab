import re
from playwright.sync_api import expect


def test_homepage_opens(browser):
    context = browser.new_context(ignore_https_errors=True)

    page = context.new_page()

    page.goto("https://orangehrm.lan.home")

    expect(page).to_have_url(re.compile(".*orangehrm.*"))

    expect(page).to_have_title(re.compile("OrangeHRM"))