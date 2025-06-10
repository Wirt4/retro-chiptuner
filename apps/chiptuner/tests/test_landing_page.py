import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_landing_page_shows_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"hello world" in response.content.lower()


def test_workflow():
    assert 4 == 5
