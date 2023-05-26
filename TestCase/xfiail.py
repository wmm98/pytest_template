import pytest


@pytest.mark.xfail(4 == 0, reason="这里有bug")
def test_xfail():
    assert 1==2
