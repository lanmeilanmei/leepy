"""
740. Delete and Earn 删除与获得点数

给定一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1:

输入: nums = [3, 4, 2]
输出: 6
解释:
删除 4 来获得 4 个点数，因此 3 也被删除。
之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
示例 2:

输入: nums = [2, 2, 3, 3, 3, 4]
输出: 9
解释:
删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
注意:

nums的长度最大为20000。
每个整数nums[i]的大小都在[1, 10000]范围内。
"""
# 这题关键要根据题意进一步拆解
# 比如, [2, 2, 3, 3, 3, 4] ==> [0, 0, 2*2, 3*3*3, 4]
# 这样就是取其中一个房间而相邻房间不可取的LC198
# Time Complexity: O(n+r), Space Complexity: O(r)


# review
class SolutionT740(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        r = max(nums)           # 方便后面初始化数组
        points = [0] * r
        for num in nums:
            points[num] += num
        return self.rob(points)

    def rob(self, nums):
        dp2, dp1 = 0, 0
        for i in range(len(nums)):
            dp = max(dp2 + nums[i], dp1)
            dp2 = dp1
            dp1 = dp
        return dp1
