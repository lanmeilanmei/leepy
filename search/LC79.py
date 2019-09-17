"""
79. Word Search
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""
# 网格搜索模板, 注意此题条件是相邻网格搜索, dfs顺序


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        h, w = len(board), len(board[0])    # 行  列
        if len(word) > h * w: return False

        def search(d, x, y):
            if x < 0 or y < 0 or x == w or y == h or word[d] != board[y][x]:  # x 列  y 行
                return False
            if d == len(word) - 1: return True

            curr = board[y][x]
            board[y][x] = ""
            found = search(d+1, x+1, y) or search(d+1, x-1, y) or search(d+1, x, y+1) or search(d+1, x, y-1)
            board[y][x] = curr
            return found

        return any(search(0, j, i) for i in range(h) for j in range(w))
