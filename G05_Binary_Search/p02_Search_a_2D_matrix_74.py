from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search of values in
        if target == matrix[0][0]:
            return True
        l_row = 0
        r_row = len(matrix) - 1
        mid_row = 0

        while l_row <= r_row:
            mid_row = (l_row + r_row) // 2
            if target < matrix[mid_row][0]:
                r_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                l_row = mid_row + 1
            else:
                break
        print(mid_row)

        nums = matrix[mid_row]
        print(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return True
        return False


def main():
    test = Solution()
    print(test.searchMatrix(matrix=[[1, 3]], target=3))
    # print(
    #     test.searchMatrix(
    #         matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    #     )
    # )
    # print(
    #     test.searchMatrix(
    #         matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    #     )
    # )
    pass


if __name__ == "__main__":
    main()
