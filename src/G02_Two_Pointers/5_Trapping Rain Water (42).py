from typing import List
from unittest import installHandler


class Solution:
    # Init
    def trap(self, height: List[int]) -> int:
        left = 0
        volume = 0
        while left < len(height) - 1:
            # print(f"-------- Outer loop----------")
            right = left + 1
            # print(f"{left=} {right=}")
            # print()
            max_value = 0
            max_value_index = 0
            while right < len(height):
                # print("--inner--")
                # print(f"{left=} {right=}")
                # find the first values that is equal to or greater if none found then the highest
                if height[right] >= height[left]:
                    max_value_index = right
                    break
                if height[right] >= max_value:
                    max_value = height[right]
                    max_value_index = right
                right += 1

            # print(f"{left=} {right=}")
            container_limit = min(height[max_value_index], height[left])
            for index in range(left + 1, max_value_index):
                if container_limit > 0:
                    volume += container_limit - height[index]

                # print(f"{volume=} with {container_limit=} and {height[index]=}")
            left = max_value_index
            # print(f"{volume=}")

        return volume


def main():
    test = Solution()
    # print(test.trap([4, 2, 0, 3, 2, 5]))
    # print(test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(test.trap([0, 2, 0]))
    # print(test.trap([4, 2, 3]))


if __name__ == "__main__":
    main()

    # tempMax = 0
    # for x in range(left + 1, len(height)):
    #     if (height[x]) >= tempMax:
    #         tempMax = height[x]
    #         new_left = x
    #     container_limit = min(height[left], height[new_left])
    #     for index in range(left + 1, new_left):
    #         volume += container_limit - height[index]
    # left = new_left
