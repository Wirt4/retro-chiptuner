from playwright.sync_api import expect


def test_record_audio_flow(custom_page):
    page = custom_page
    uploads = []

    # set an intercepter to catch the uploads
    def handle_upload(route, request):
        uploads.append(request)
        route.continue_()

    # listen to the "**/upload_audio" route
    page.route("**/upload_audio", handle_upload)

    page.goto("http://localhost:8000")
    page.click("text=Record")
    page.wait_for_timeout(3000)
    page.click("text=Stop")
    page.wait_for_timeout(1000)

    assert len(uploads) > 0, "No upload request was captured"
