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


test = Solution()
print(test.containsDuplicate([1, 2, 3, 1]))
print(test.containsDuplicate([1, 2, 3, 4]))
print(test.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
