import pytest

from app.add import add


def test_add():
    assert add(0.3, 0.4) == pytest.approx(0.7)
