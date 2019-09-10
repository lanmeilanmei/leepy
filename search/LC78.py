"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
# lc77 lc39 lc40 lc17 BFS


class SolutionT78(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(nums)+1):
            self.dfs(nums, 0, i, 0, [], ans)
        return ans

    def dfs(self, nums, depth, n, start, path, ans):
        if depth == n:
            ans.append(path[:])
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, depth+1, n, i+1, path, ans)
            path.pop()

    def subsets_BFS(self, nums):
        if not nums: return []
        ans = [[]]
        for num in nums:
            tmp = []
            for path in ans:
                tmp.append(path+[num])
            ans += tmp
        return ans
