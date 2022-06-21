from typing import List


class Solution:
    # Initial attempt
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]


def main():
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
    # print(test.twoSum([3, 2, 4], 6))
    # print(test.twoSum([3, 3], 6))


if __name__ == "__main__":
    main()
