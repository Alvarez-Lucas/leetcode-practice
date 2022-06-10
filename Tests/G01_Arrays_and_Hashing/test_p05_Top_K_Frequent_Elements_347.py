import pytest


from src.G01_Arrays_and_Hashing.p05_Top_K_Frequent_Elements_347 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_topKFrequent_example_1(solution):
    assert solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]


def test_topKFrequent_example_2(solution):
    assert solution.topKFrequent(nums=[1], k=1) == [1]
