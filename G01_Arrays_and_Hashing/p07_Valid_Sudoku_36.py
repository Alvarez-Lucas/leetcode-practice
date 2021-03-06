from typing import List

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board3 = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            x = set()
            for element in row:
                if element != "." and element in x:
                    return False
                else:
                    x.add(element)
        for i in range(len(board[0])):
            x = set()
            for row in board:
                if row[i] != "." and row[i] in x:
                    return False
                else:
                    x.add(row[i])
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                map = set()
                for inner_x in range(x, x + 3):
                    for inner_y in range(y, y + 3):
                        if (
                            board[inner_x][inner_y] != "."
                            and board[inner_x][inner_y] in map
                        ):
                            return False
                        else:
                            map.add(board[inner_x][inner_y])
        return True


def main():
    test = Solution()
    print(test.isValidSudoku(board))
    print(test.isValidSudoku(board2))
    print(test.isValidSudoku(board3))


if __name__ == "__main__":
    main()
