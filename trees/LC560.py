"""
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
# notes:
# subarraySum 源自LC437
# BruteForce  --> 检查每对(i, j)的sum(nums[i:j]), complexity: O(n^3), Space complexity: O(1) 超时LTE
# BrutePrefix --> 先记录连续累加和, 再暴力查找 Time complexity: O(n^2), Space complexity: O(n)
# PrefixSum   --> 记录连续累加和, 如果(当前累加和 - target)被PrefixSum字典记录, 则说明存在连续路径


# TODO 未完全理解熟悉
class SolutionT560(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def helper(nums, i, so_far, target):
            if i >= len(nums): return
            so_far += nums[i]
            if so_far - target in self.cache:
                self.ct += self.cache[so_far - target]
            self.cache[so_far] = self.cache.get(so_far, 0) + 1
            helper(nums, i+1, so_far, target)
            self.cache[so_far] = self.cache.get(so_far, 0) - 1

        self.ct = 0
        self.cache = {0: 1}
        helper(nums, 0, 0, k)
        return self.ct

    def subarraySum_BruteForce(self, nums, k): # LTE
        ct = 0
        i, j = 0, 1
        while i < len(nums):
            if j > len(nums):
                i += 1
                j = i + 1
            if nums[i:j] and sum(nums[i:j]) == k:   # 检查nums[i:j]避免出现[]情况
                ct += 1
            j += 1
        return ct

    def subarraySum_BrutePrefix(self, nums, k):
        N = len(nums)
        prefixSum = [0] * (N + 1)
        for i in range(1, N+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]   # 记录连续相邻累加和
        ct = 0
        for i in range(N):
            for j in range(i, N):
                if prefixSum[j+1] - prefixSum[i] == k:
                    ct += 1
        return ct

    def subarraySum_PrefixSum(self, nums, k):
        prefixSum = {0: 1}
        ct = so_far = 0
        for num in nums:
            so_far += num
            if so_far - k in prefixSum:
                ct += prefixSum[so_far - k]
            prefixSum[so_far] = prefixSum.get(so_far, 0) + 1
        return ct
