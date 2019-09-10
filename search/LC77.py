"""
77. Combinations 组合

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
# 组合搜索问题 lc17 lc39 lc40


class SolutionT77(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(n, 1, 0, k, [], ans)
        return ans

    def dfs(self, n, start, depth, k, path, ans):
        if depth == k:
            ans.append(path[:])
            return

        for i in range(start, n+1):
            path.append(i)
            self.dfs(n, i+1, depth+1, k, path, ans)
            path.pop()
