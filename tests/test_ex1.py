# import pytest

# @pytest.fixture(scope="session")
# def fixture_1():
#     print('run-fixture-1')
#     return 1

# def test_example1(fixture_1):
#     print("example1")
#     num = fixture_1
#     assert num == 1

# def test_example2(fixture_1):
#     print("example2")
#     num = fixture_1
#     assert num == 1


# @pytest.mark.skip
# def test_one_plus_one():
#     print('test one')
#     number = 1 + 1
#     assert number == 2

# @pytest.mark.xfail
# def test_failure_one_plus_one():
#     number = 1 + 1
#     assert number == 2