import pytest


from src.G01_Arrays_and_Hashing.p03_Two_Sum_1 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_twoSum_example_1(solution):
    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]


def test_twoSum_example_2(solution):
    assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]


def test_twoSum_example_3(solution):
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
