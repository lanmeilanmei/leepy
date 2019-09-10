"""
47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
# if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
# 这里的去重保证。从反面来看,如果有重复元素且前者已经被使用, 则可继续执行调用后面的dfs, 否则不进行dfs


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums, 0, len(nums), [False]*len(nums), [], ans)
        return ans

    def dfs(self, nums, depth, n, used, path, ans):
        if depth == n:
            ans.append(path[:])
            return

        for i in range(len(nums)):
            if used[i] is True: continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue   # 确保位置只有靠前的重复元素先被使用
            used[i] = True
            path.append(nums[i])
            self.dfs(nums, depth+1, n, used, path, ans)
            path.pop()
            used[i] = False
