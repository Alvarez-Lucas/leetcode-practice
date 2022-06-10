from typing import List


class Solution:
    # init
    def twoSumInit(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while numbers[left_pointer] + numbers[right_pointer] != target:
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
        return [left_pointer + 1, right_pointer + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while left_pointer < right_pointer:
            current_sum = numbers[left_pointer] + numbers[right_pointer]
            if current_sum > target:
                right_pointer -= 1
            elif current_sum < target:
                left_pointer += 1
            else:
                return [left_pointer + 1, right_pointer + 1]


def main():
    test = Solution()
    print(test.twoSum(numbers=[2, 7, 11, 15], target=9))


if __name__ == "__main__":
    main()
