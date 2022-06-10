from typing import List
from unittest import result


class Solution:
    # init
    def maxAreaInit(self, height: List[int]) -> int:
        current_max = 0
        for left_boundary in range(len(height) - 2):
            r = len(height) - 1
            while r > left_boundary:
                to_test = (r - left_boundary) * min(height[left_boundary], height[r])
                current_max = max(to_test, current_max)
                r -= 1
        return current_max

    # Solution
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
        return result


def main():
    test = Solution()
    test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])


if __name__ == "__main__":
    main()
