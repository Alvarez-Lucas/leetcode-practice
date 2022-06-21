from typing import List


class Solution:
    def minEatingSpeedInit(self, piles: List[int], h: int) -> int:
        maxk = max(piles)

        def get_h(k):
            h = 0
            temp = piles.copy()
            index = 0

            while sum(temp) > 0:
                while index < len(temp) and temp[index] > 0:
                    temp[index] -= k
                    if temp[index] < 0:
                        temp[index] = 0
                    h += 1
                index += 1
            return h

        for k in range(1, maxk + 1):
            # print(f"testing {k}")
            if get_h(k) == h:
                return k

        return -1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        while l <= r:
            k = (l + r) // 2
            banana = piles[k] / h
            currentH
            for pile in piles:
                currentH = pile / k


def main():
    test = Solution()
    print(test.minEatingSpeed(piles=[3, 6, 7, 11], h=8))

    print(test.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))

    print(test.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))


if __name__ == "__main__":
    main()
