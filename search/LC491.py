"""
491. 递增子序列

给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""
# 组合搜索模板, 而且是单元素不能多次重复被查找、并保持先后顺序的案例,


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.N = len(nums)
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans

    def dfs(self, nums, start, path, ans):
        if len(path) >= 2:
            ans.append(path[:])

        used = set()
        for i in range(start, self.N):
            if nums[i] in used: continue
            if not path or nums[i] >= path[-1]:
                used.add(nums[i])
                path.append(nums[i])
                self.dfs(nums, i+1, path, ans)
                path.pop()

    def bfs(self, nums):
        ans = {()}
        for num in nums:
            tmp = {()}
            for path in ans:
                if not path or path[-1] <= num:
                    tmp.add(path + (num, ))
            ans |= tmp

        return [p for p in ans if len(p) >= 2]
