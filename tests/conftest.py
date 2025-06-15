import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # Change to True in CI
            args=[
                "--use-fake-ui-for-media-stream",
                "--use-fake-device-for-media-stream",
                "--use-file-for-fake-audio-capture=./tests/assets/test_audio.wav",
            ],
        )
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture
def custom_page(browser_context) -> Page:
    page = browser_context.new_page()
    yield page
    page.close()
