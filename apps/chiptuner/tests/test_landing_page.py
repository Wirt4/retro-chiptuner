import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


@pytest.mark.django_db
def test_landing_page_shows_record_button(client):
    # visit the site root
    response = client.get(reverse("landing"))
    # confirm the status is okay
    assert response.status_code == 200

    # parse the page
    soup = BeautifulSoup(response.content, "html.parser")
    record_button = soup.find(
        lambda tag: tag.name in ["button", "a"] and tag.text.strip().lower() == "record"
    )
    assert record_button is not None, "Button with label 'record' not found"
