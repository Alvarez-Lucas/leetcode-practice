from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(f"{ nums= }")
        print(f"{ target= }")
        if nums[0] == target:
            return 0

        l = 0
        r = len(nums) - 1
        while l <= r:
            # mid = (l + r) // 2
            mid = l + ((r - l) // 2)
            print(f"begin loop")

            if nums[mid] == target:
                print(f"case A {mid=} {l=} {r=} {nums[mid]=}")
                return mid
            elif target < nums[mid] and target >= nums[l]:
                print(f"case B {mid=} {l=} {r=} {nums[mid]=}")
                r = mid - 1
            elif target < nums[mid] and target < nums[l]:
                print(f"case C {mid=} {l=} {r=} {nums[mid]=}")
                l = mid + 1
            elif target > nums[mid] and target <= nums[r]:
                print(f"case D {mid=} {l=} {r=} {nums[mid]=}")
                l = mid + 1
            else:
                print(f"faggot {mid=} {l=} {r=} {nums[mid]=}")
                r = mid - 1
            print()
        print(f"{mid=} {l=} {r=}")

        return -1


def main():
    test = Solution()
    # print(test.search([1, 3], 3))
    print(test.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
    # print(test.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    # print(test.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))


if __name__ == "__main__":
    main()
