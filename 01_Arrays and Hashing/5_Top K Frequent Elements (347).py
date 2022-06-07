from typing import List
from collections import defaultdict


class Solution:
    # Init
    def topKFrequentInit(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        for number in nums:
            count[number] += 1
        final = [
            key
            for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True)
        ]
        return final[0:k]

    # Other Solution
    # Double arrays where the index is the count, reverse it 
    # Traverse it and pop values to append to result
    # while values in the inner list exists and 
    # while K has not been fully decremented
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outer_array = [[] for _ in range(len(nums) + 1)]
        counter = {}

        for num in nums:
            counter[num] = 1 if num not in counter else counter[num] + 1
        for value, count in counter.items():
            outer_array[count].append(value)
        result = []
        for inner_array in reversed(outer_array):
            while inner_array and k > 0:
                result.append(inner_array.pop())
                k -= 1
            if k == 0:
                break
        return result


def main():
    test = Solution()
    print(test.topKFrequent([2, 2, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2], 2))


if __name__ == "__main__":
    main()
