import pytest


from src.G01_Arrays_and_Hashing.p04_Group_Anagrams_49 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_groupAnagrams_example_1(solution):
    """
    Order of outer lists matter here in this test when they should not,
    not the most optimal test case
    in other words, not all valid answerers are registered as valid
    # TODO expand test case to account for any order
    """
    return_value = solution.groupAnagrams(
        strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    )
    answer_key = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    for sub_list_test, sub_list_answer in zip(return_value, answer_key):
        assert all(string in sub_list_answer for string in sub_list_test)
        assert all(string in sub_list_test for string in sub_list_answer)


def test_groupAnagrams_example_2(solution):
    assert solution.groupAnagrams(strs=[""]) == [[""]]


def test_groupAnagrams_example_3(solution):
    assert solution.groupAnagrams(strs=["a"]) == [["a"]]
