"""
300. 最长上升子序列

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
# DFS
# BFS


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans[i] = max(ans[i], ans[j] + 1)
        return max(ans)

    def lengthOfLIS_dfs(self, nums):
        def dfs(arr, r):    # 找到比当前 r 位置小的最长升序子序列的元素个数
            if r == 0:
                return 1
            if f[r] > 0:
                return f[r]

            ct = 1
            for j in range(r):
                if arr[r] > arr[j]:
                    ct = max(ct, dfs(arr, j) + 1)
            f[r] = ct
            return f[r]

        if not nums: return 0
        n = len(nums)
        f = [0] * n
        ans = 0

        for i in range(n):
            ans = max(ans, dfs(nums, i))
        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLIS_dfs([10, 9, 2, 5, 3, 7, 101, 18]))
