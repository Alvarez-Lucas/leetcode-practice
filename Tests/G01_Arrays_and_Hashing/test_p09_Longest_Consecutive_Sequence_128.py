import pytest


from src.G01_Arrays_and_Hashing.p09_Longest_Consecutive_Sequence_128 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_longestConsecutive_example_1(solution):
    assert solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4


def test_longestConsecutive_example_2(solution):
    assert solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
