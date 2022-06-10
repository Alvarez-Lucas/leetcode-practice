class Solution:
    # My initial solution
    def isAnagramInit(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s, and false otherwise."""
        if len(s) != len(t):
            return False
        letters = {}
        for char in s:
            letters[char] = 1 if char not in letters else letters[char] + 1
        for char in t:
            if char not in letters or letters[char] <= 0:
                return False
            letters[char] -= 1
        return True

    # Slightly modified source solution
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s, and false otherwise."""
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for charS, charT in zip(s, t):
            countS[charS] = 1 + countS.get(charS, 0)
            countT[charT] = 1 + countT.get(charT, 0)
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
        return True


def main():
    test = Solution()
    print(test.isAnagram("hello", "lhelo"))


if __name__ == "__main__":
    main()
