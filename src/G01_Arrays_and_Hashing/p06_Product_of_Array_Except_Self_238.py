from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        for i in range(len(nums)):
            print(i)
        return nums


def main():
    test = Solution()
    print(test.productExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
