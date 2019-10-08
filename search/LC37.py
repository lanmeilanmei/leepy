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
# 官方代码, https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode/


# official
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

    def solveSudoku_official(self, board):
        from collections import defaultdict

        def could_place(d, row, col):
            """ 检查是否能够在(row, col)处放置数字d, 需要检查行、列、块 """
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """ 在(row, col)处放置数字d """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """ 移除不符合条件的数字d """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = "."

        def place_next_number(row, col):
            """ 递归调用backtrack函数, 继续放置数字直至有解 """
            # 遍历完最后一个位置, 有解
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:    # 当前列位置遍历完, 则行数进位
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col+1)

        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for dd in range(1, 10):
                    if could_place(dd, row, col):
                        place_number(dd, row, col)
                        place_next_number(row, col)

                        if not sudoku_solved:
                            remove_number(dd, row, col)
            else:
                place_next_number(row, col)

        n = 3
        N = n * n
        box_index = lambda row, col: (row // n) * n + col // n # 计算块的索引匿名函数

        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        # 记录初始九宫格状态
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()


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
