"""
53. Maximum Subarray  最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
# 最优公式：当前累加和 = 之前累加和+当前值  和  当前值  的较大者
# 因为求连序最大和
# 解法1 DP之记忆递归 Time complexity: O(n), Space complexity: O(n)
# 解法2 Time complexity: O(n), Space complexity: O(1)


class SolutionT153(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = nums[:]
        for i in range(1, len(nums)):
            sums[i] = max(sums[i-1] + nums[i], nums[i])
        return max(sums)

    def maxSubArray_2(self, nums):
        res = cursum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            res = max(res, cursum)
        return res
