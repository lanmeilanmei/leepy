"""

"""
# 解法1: dfs穷举 时间复杂度：O(2^n), 递归树的大小将为 2^n ,空间复杂度：O(n^2) 使用大小为 n*nn∗n 的 memomemo 数组
# 解法2: bfs穷举


# unfinished
class Solution(object):
    # 超时
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(arr, pre, curr):
            if curr == len(arr):
                return 0

            taken = 0
            if arr[curr] > pre:
                taken = 1 + dfs(arr, arr[curr], curr+1)

            notaken = dfs(arr, pre, curr+1)
            return max(taken, notaken)

        return dfs(nums, -float("inf"), 0)

    def lengthOfLIS_Square(self, nums):
        if not nums: return 0
        n = len(nums)
        f = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:   # 这里f[i]要记录不超过nums[i]的最长升序子序列长度
                    a, b = f[i], f[j] + 1
                    f[i] = max(a, b)  # 注意这里的选取, 先理解f[i]含义.

        return max(f)


if __name__ == '__main__':
    # print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 4]))

    # print(Solution().lengthOfLIS_Square([10, 9, 2, 5, 3, 4]))

    print(Solution().lengthOfLIS_Square([1, 3, 6, 7, 9, 4, 10, 5, 6]))
