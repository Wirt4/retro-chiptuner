import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


@pytest.mark.django_db
def test_temp(client):
    """
    Given the landing page response is 200, when the page loads, then it will have button named "playback".
    """
    response = client.get(reverse("landing"))
    assert response.status_code == 200

    html_parser = BeautifulSoup(response.content, "html.parser")
    button_name = "playback"
    button = html_parser.find(
        lambda tag: tag.name in ["button", "a"]
        and tag.text.strip().lower() == button_name
    )
    assert button is not None, 'button "{}" is not found'.format(button_name)
