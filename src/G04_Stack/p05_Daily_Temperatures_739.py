from typing import List


class Solution:
    # Init - too slow, O(n**2)
    def dailyTemperaturesInit(self, temperatures: List[int]) -> List[int]:
        res = []
        for l, temp in enumerate(temperatures):
            r = l + 1
            while r < len(temperatures) and temperatures[r] <= temp:
                r += 1

            if r == len(temperatures):
                res.append(0)
            else:
                res.append(r - l)
        return res

    # TODO: Look at source
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass


def main():
    test = Solution()
    print(test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


if __name__ == "__main__":
    main()
