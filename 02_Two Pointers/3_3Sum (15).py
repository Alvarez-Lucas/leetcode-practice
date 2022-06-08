from lib2to3.pgen2.token import LBRACE
import re
from typing import List


class Solution:
    # init
    def threeSumInit(self, nums: List[int]) -> List[List[int]]:
        results = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    print(f"{i=} {j=} {k=}")
                    sorted_shit = sorted([nums[i], nums[j], nums[k]])
                    key = str(sorted_shit)
                    if nums[i] + nums[j] + nums[k] == 0 and key not in results:
                        print([nums[i], nums[j], nums[k]])
                        results[key] = sorted_shit
        return results.values()

    # Solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    results.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return results

    # also tried reusing old two sums on nums[i+1:], with the target being 0-nums[i]


def main():
    test = Solution()
    # print(test.threeSum([-1, 0, 1, 2, -1, -4]))
    print(test.threeSum([-2, 0, 1, 1, 2]))


if __name__ == "__main__":
    main()
