from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif token == "+":
                temp = stack.pop() + stack.pop()
                stack.append(int(temp))
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif token == "*":
                temp = stack.pop() * stack.pop()
                stack.append(int(temp))
            else:
                stack.append(int(token))
        return stack[0]


def main():
    test = Solution()
    print(test.evalRPN(["2", "1", "+", "3", "*"]))
    print(test.evalRPN(["4", "13", "5", "/", "+"]))
    print(
        test.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )


if __name__ == "__main__":
    main()
