from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while numbers[left_pointer] + numbers[right_pointer] != target:
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
                print("yah")
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
                print("has")
            else:
                print("asd")
        return [left_pointer + 1, right_pointer + 1]


def main():
    test = Solution()
    print(test.twoSum(numbers=[2, 7, 11, 15], target=9))


if __name__ == "__main__":
    main()
