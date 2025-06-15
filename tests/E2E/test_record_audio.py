from playwright.sync_api import expect


def test_record_audio_flow(custom_page):
    page = custom_page
    page.goto("http://localhost:8000")
    locator = page.get_by_role("button", name="Stop")
    expect(locator).to_have_count(0)
    page.click("text=Record")
    page.wait_for_timeout(30)
    page.click("text=Stop")
