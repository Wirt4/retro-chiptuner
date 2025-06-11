import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


class LandingPage:
    def __init__(self, client):
        response = client.get(reverse("landing"))
        assert response.status_code == 200
        self._soup = BeautifulSoup(response.content, "html.parser")

    def assert_has_button(self, button_name):
        """
        Given the response has been successfully pulled from the landing page, when the function is called, then the button is located in the page response.

        The assertion fails if the button is not there.
        """
        button = self._soup.find(
            lambda tag: tag.name in ["button", "a"]
            and tag.text.strip().lower() == button_name
        )
        assert button is not None, "Button with label {} not found".format(button_name)


@pytest.mark.django_db
def test_landing_page_has_buttons(client):
    """
    Given the landing page response is 200, when the page loads, then it will have buttons named "record" and "playback".
    """
    page = LandingPage(client)
    page.assert_has_button("record")
    page.assert_has_button("playback")
