"""
216. Combination Sum III 组合总和 III

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""
# lc39 lc40


class SolutionT216(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(n, 1, 0, k, [], ans)
        return ans

    def dfs(self, target, start, depth, n, path, ans):
        if depth == n:                  # 这里用递归深度做提前退出条件
            if target == 0:
                ans.append(path[:])
            return

        for num in range(start, 10):
            if num > target: break
            path.append(num)
            self.dfs(target-num, num+1, depth+1, n, path, ans)
            path.pop()

