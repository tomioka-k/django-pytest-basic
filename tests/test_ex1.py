import pytest

@pytest.mark.skip
def test_one_plus_one():
    print('test one')
    number = 1 + 1
    assert number == 2

@pytest.mark.xfail
def test_failure_one_plus_one():
    number = 1 + 1
    assert number == 2