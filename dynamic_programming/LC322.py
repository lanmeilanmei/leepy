"""
322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
"""
# 解法1: O(n * amount^2)


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(amount-coin, -1, -1):    # 当前剩余面额总数
                if dp[i] != (amount+1):
                    for k in range(1, amount//coin + 1):     # 硬币个数
                        p = k * coin + i    # 记住这个公式, i 是降序的
                        if p <= amount:
                            dp[p] = min(dp[p], dp[i] + k)    #

        return -1 if dp[amount] == (amount+1) else dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))

    print(Solution().coinChange([12], 11))
