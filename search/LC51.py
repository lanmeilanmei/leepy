"""
51. N皇后问题

由于问题较为常见, 这里直接贴官方解题链接
https://leetcode-cn.com/problems/n-queens/solution/nhuang-hou-by-leetcode/
"""
# dfs + 回溯法   LC37
# 注意 backtrack 跳转到 remove_queen 的情况


# official
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row-col] + dale_diagonals[row+col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row-col] = 1
            dale_diagonals[row+col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row-col] = 0
            dale_diagonals[row+col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append("." * col + "Q" + "." * (n-col-1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    # 当全部走完或者下一行全部失败(表示当前放置位是不合适的), 因此需要从下一层回溯到该层, 删除当前层位置, 并重新寻找合适位置
                    remove_queen(row, col)      # 可能回溯到这一步的条件: 在该层的基础上下一层选择完全不合适 or 下一步得到了可能解需要再找其它解

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1) # 对角线row、col组合计算的最大值为 2 * (n-1)
        dale_diagonals = [0] * (2 * n - 1)

        queens = set()
        output = []
        backtrack()
        return output


print(Solution().solveNQueens(4))
