class Solution:
    # init
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for char in s:
            if stack and matching.get(char, 0) == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

    # Could return early if invalid


def main():
    test = Solution()
    print(test.isValid("()"))
    print(test.isValid("()[]{}"))
    print(test.isValid("(]"))


if __name__ == "__main__":
    main()
