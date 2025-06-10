import pytest


def f():
    pass


def test_mytest():
    with pytest.raises(SystemExit):
        f()


# Create your tests here.
