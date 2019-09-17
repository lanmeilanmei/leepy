"""
37. Sudoku Solver 解数独

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
"""


# unresolved
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.rows = [[0 for _ in range(10)] for _ in range(9)]
        self.cols = [[0 for _ in range(10)] for _ in range(9)]
        self.boxes = [[0 for _ in range(10)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    n = int(c)
                    bx = j // 3
                    by = i // 3
                    self.rows[i][n] = 1
                    self.cols[j][n] = 1
                    self.boxes[by * 3 + bx][n] = 1
        self.fill(board, 0, 0)

    def fill(self, board, x, y):
        if y == 9: return True

        nx = (x + 1) % 9
        ny = y + 1 if nx == 0 else y

        if board[y][x] != ".": self.fill(board, nx, ny)

        for i in range(1, 10):
            bx = x // 3
            by = y // 3
            box_key = by * 3 + bx

            if not self.rows[y][i] and not self.cols[x][i] and not self.boxes[box_key][i]:
                self.rows[y][i] = 1
                self.cols[x][i] = 1
                self.boxes[box_key][i] = 1
                board[y][x] = str(i)
                if self.fill(board, nx, ny): return True
                board[y][x] = "."
                self.boxes[box_key][i] = 0
                self.cols[x][i] = 0
                self.rows[y][i] = 0
        return False


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print(board)
