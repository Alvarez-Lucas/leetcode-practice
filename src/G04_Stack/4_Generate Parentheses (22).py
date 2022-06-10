from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = ["(" for _ in range(n)]
        stack_right = [["("] * n]
        print(stack)
        print(stack_right)

        matching = {"(": "L", ")": "R"}
        something = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        for valid in something:
            for char in valid:
                print(matching[char], end="")
            print()


def main():
    test = Solution()
    print(test.generateParenthesis(3))
    pass


if __name__ == "__main__":
    main()
