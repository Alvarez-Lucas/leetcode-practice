from typing import List


class Solution:
    def searchSomething(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        print(f"{nums=} {mid=}")
        print(mid)
        if target < nums[mid]:
            self.searchSomething(nums[:mid], target)
        elif target > nums[mid]:
            self.searchSomething(nums[mid:], target)
        else:
            print(mid)
            return mid

    def search(self, nums: List[int], target: int) -> int:
        index = len(nums) // 2
        segment_distance = len(nums)

        def binSearch(index, segment_distance):
            segment_distance = segment_distance // 2
            print(f"{segment_distance=} {index=} ")
            if nums[index] == target:
                return index
            elif nums[index] < target:
                index += segment_distance
                print(f" going up {index=}")
                binSearch(index, segment_distance)
            elif nums[index] > target:
                index -= segment_distance
                print(f" going down {index=}")
                binSearch(index, segment_distance)

        binSearch(index, segment_distance=segment_distance)


def main():
    test = Solution()
    test.search(nums=[-1, 0, 3, 5, 9, 12], target=9)
    pass


if __name__ == "__main__":
    main()
