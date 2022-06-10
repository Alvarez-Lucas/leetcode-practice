import pytest


from src.G01_Arrays_and_Hashing.p06_Product_of_Array_Except_Self_238 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_productExceptSelf_example_1(solution):
    assert solution.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]


def test_productExceptSelf_example_2(solution):
    assert solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
