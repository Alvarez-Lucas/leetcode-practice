class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s, and false otherwise."""
        letters = {}
        if len(s) != len(t):
            return False
        for char in s:
            letters[char] = 1 if char not in letters else letters[char] + 1
        for char in t:
            if char not in letters or letters[char] <= 0:
                return False
            letters[char] -= 1
        return True


def main():
    test = Solution()
    print(test.isAnagram("hello", "lhelo"))


if __name__ == "__main__":
    main()
