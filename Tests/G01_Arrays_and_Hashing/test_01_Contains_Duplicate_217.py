import pytest


from src.G01_Arrays_and_Hashing.p01_Contains_Duplicate_217 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.containsDuplicate([1, 2, 3, 1]) == True


def test_example_2(solution):
    assert solution.containsDuplicate([1, 2, 3, 4]) == False


def test_example_3(solution):
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
