import pytest


from src.G01_Arrays_and_Hashing.p02_Valid_Anagram_242 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_isAnagram_example_1(solution):
    assert solution.isAnagram(s="anagram", t="nagaram") == True


def test_isAnagram_example_2(solution):
    assert solution.isAnagram(s="rat", t="car") == False
