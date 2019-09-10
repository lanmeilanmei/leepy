"""
90. 子集 II

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
# lc40 避免重复组合


class SolutionT90(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)+1):
            self.dfs(nums, 0, i, 0, [], ans)
        return ans

    def dfs(self, nums, depth, n, start, path, ans):
        if depth == n:
            ans.append(path[:])
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue  # 这里两个条件共同限制避免重复情况
            path.append(nums[i])
            self.dfs(nums, depth+1, n, i+1, path, ans)
            path.pop()
