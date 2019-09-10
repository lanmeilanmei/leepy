"""
46. 全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
# 全排列搜索模板
# 注意与组合搜索的dfs的差异 lc39 + BFS中全排列的实现差异 lc78


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums, 0, len(nums), [False] * len(nums), [], ans)
        return ans

    def dfs(self, nums, depth, n, used, path, ans):
        if depth == n:
            ans.append(path[:])
            return

        for i in range(len(nums)):
            if used[i] is True: continue
            used[i] = True
            path.append(nums[i])
            self.dfs(nums, depth+1, n, used, path, ans)
            path.pop()
            used[i] = False

    def permute_BFS(self, nums):
        ans = [[]]
        for num in nums:
            tmp = []
            for path in ans:
                for i in range(len(path)+1):                    # 可最多追加元素到末尾
                    tmp.append(path[:i] + [num] + path[i:])     # 实现位置的追加操作
            ans = tmp                                           # 固定长度是更新ans, 变长则是添加到ans
        return ans
