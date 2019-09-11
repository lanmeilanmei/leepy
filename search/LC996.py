"""
996. 正方形数组的数目

给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。

返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。

示例 1：

输入：[1,17,8]
输出：2
解释：
[1,8,17] 和 [17,8,1] 都是有效的排列。
示例 2：

输入：[2,2,2]
输出：1
 

提示：

1 <= A.length <= 12
0 <= A[i] <= 1e9
"""
# 和lc943一样, 由于输入空间最多允许12个元素, dfs搜索结果勉强通过, 还是得DP来优化
from math import sqrt


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = []
        self.N = len(A)
        self.dfs(A, 0, self.N, [False] * self.N, [], ans)
        return len(ans)

    def dfs(self, nums, depth, n, used, path, ans):
        if depth == n:
            if path not in ans:
                ans.append(path[:])
            return

        for i in range(self.N):
            if used[i] is True: continue
            if i > 0 and not used[i-1] and nums[i] == nums[i-1]: continue       # 剪枝
            if path and not self.isSquareArr(nums[i], path[-1]): continue       # 平方数组定义剪枝
            # if not path or self.isSquareArr(nums[i], path[-1]):
            # if (i == 0) or (i > 0 and self.isSquareArr(nums[i], path[-1])):
            used[i] = True
            path.append(nums[i])
            self.dfs(nums, depth+1, n, used, path, ans)
            path.pop()
            used[i] = False

    # 也可以通过两数之和是否等于平方数判断
    def isSquareArr(self, a1, a2):
        summary = a1 + a2
        return True if summary == 0 or summary % sqrt(summary) == 0 else False      # 考虑到0值情况
