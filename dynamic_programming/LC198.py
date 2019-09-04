"""
198. House Robber 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
# f(i) = max(f(i-1), f(i-2)+nums[i])
# 解法1、2、3 思路见 LC121, 解法4的记忆化递归超时了


# review
class SolutionT198(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n <= 2: return max(nums)
        front, later = nums[0], nums[1]             # 当前房间的前前房间[不相邻]，当前房间的前房间[相邻]
        for i in range(2, len(nums)):
            better = max(front + nums[i], later)    # 最大金额状态公式, 当前可以窃取或不窃取
            front = max(front, later)               # 更新前前房间的最大金额, 方便下次状态比较
            later = better
        return later

    # 同上 by hh
    def rob_1(self, nums):
        if not nums: return 0
        dp1, dp2 = 0, 0
        for i in range(len(nums)):
            dp = max(dp2 + nums[i], dp1)            # 最大金额状态公式, 当前可以窃取或不窃取
            dp2 = dp1                               # 这里dp1初始化就是前相邻房间已累计窃取最大金额, 与上面有所不同
            dp1 = dp
        return dp1

    # 初始是滚动数组解法，这里是滚动数组的数组解法[memorized]
    def rob_2(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n <= 2: return max(nums)
        dp = nums[:]
        dp[1] = dp[1] if dp[1] > dp[0] else dp[0]
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]) # 最严谨的状态转移公式, 注意dp[0]和dp[1]的初始化铺垫
            # dp[i-2] = max(dp[i-1], dp[i-2])
            # dp[i - 2] = dp[i-1]                   # 注释的是错的, 被自己解法1蒙蔽了双眼.[尽管凑凑也能过]
            # dp[i-1] = dp[i]
        return dp[n-1]

    # 记忆化递归
    def rob_3(self, nums):
        n = len(nums)
        self.dp = [-1] * n
        return self.recursive(nums, n-1)

    def recursive(self, nums, i):
        if i < 0: return 0
        if self.dp[i] > 0: return self.dp[i]
        self.dp[i] = max(self.recursive(nums, i-2) + nums[i], self.recursive(nums, i-1))
        return self.dp[i]
