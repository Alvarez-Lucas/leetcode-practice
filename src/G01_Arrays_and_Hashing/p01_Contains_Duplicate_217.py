import unittest

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        visited = set()

        for val in nums:
            if val in visited:
                return True
            visited.add(val)
        return False
