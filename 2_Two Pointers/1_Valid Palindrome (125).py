import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Given a string s, return true if it is a palindrome, or false otherwise."""
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


test = Solution()

print(test.isPalindrome("race car"))
