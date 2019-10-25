"""
示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
"""
# 解法1: O(n*amount^2)


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0: return 0
        dp = [2 * amount] * (amount + 1)
        dp[0] = 0

        for num in coins:
            for i in range(amount-num, -1, -1):     # 与个数k搭配后当前剩余面额
                if dp[i] != 2 * amount:
                    for k in range(1, amount // num):   # 已使用的硬币个数
                        p = k * num + i     # 当前实际累计面额
                        if p <= amount:
                            dp[p] = min(dp[p], dp[i] + k)

        return dp[amount] if dp[amount] != 2 * amount else -1


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
