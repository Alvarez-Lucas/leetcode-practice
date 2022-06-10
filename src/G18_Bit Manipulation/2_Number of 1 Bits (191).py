class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count("1")
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result


def main():
    test = Solution()
    test.hammingWeight()


if __name__ == "__main__":
    main()
