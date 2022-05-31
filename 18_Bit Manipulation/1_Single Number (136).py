from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Given a non-empty array of integers nums, every element appears twice except for one. Find that single one."""
        current = 0
        for val in nums:
            current ^= val
        return current


def main():
    test = Solution()
    print(test.singleNumber([2, 2, 1]))
    print(test.singleNumber([4, 1, 2, 1, 2]))
    print(test.singleNumber([1]))


if __name__ == "__main__":
    main()
