"""
针对股票利润系列题的解法 ⭐
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
"""
"""
base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

状态转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""
"""  从穷举所有可能的取值 ----> 穷举所有的状态 [DP思路转化]
天数i、交易次数k、股票持有状态state
T121 ---> k<=1
T122 ---> k<=float("inf")
T123 ---> K<=2
T188 ---> K<=m
T309 ---> state cold
T714 ---> state fee
"""


class SolutionT121(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        # dp = [[0, 0]] * n # 会带来子数组复制

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i]) # 只允许最多一次交易
        return dp[n-1][0]

        # 下面也阔以, 初始化有区别
        # dp[-1][0] = 0
        # dp[-1][1] = -float("inf")
        # for i in range(n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], -prices[i])  # 只允许最多一次交易
        # return dp[n - 1][0]

    def maxProfit2(self, prices):
        if not prices: return 0
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float("inf")

        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0


class SolutionT122(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])  # 允许多次交易
        return dp[n - 1][0]

    def maxProfit2(self, prices):
        if not prices: return 0
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float("inf")      # 注意双变量解法的初始状态

        for i in range(n):
            tmp = dp_i_0      # 注意临时状态值作用
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp-prices[i])
        return dp_i_0


class SolutionT123(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        max_k = 2

        dp = [[[0, 0] for _ in range(max_k+1)] for _ in range(n)]

        # for i in range(n):
        #     for k in range(max_k, 0, -1):
        #         if i == 0:
        #             dp[i][k][0] = 0
        #             dp[i][k][1] = -prices[0]
        #             continue
        #         dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #         dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # return dp[n-1][max_k][0]

        for i in range(n):
            for k in range(1, max_k+1): # 上面官方是倒序初始化, 可读性略差. 但k=0时初始值都应该是0, 这样才能初始化后续k值交易
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[0]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][max_k][0]

    class SolutionT188(object):
        def maxProfit(self, k, prices):     # testCases 209/211, 因为k过大时会超内存
            """
            :type k: int
            :type prices: List[int]
            :rtype: int
            """
            if not prices: return 0
            n = len(prices)
            max_k = k

            dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(n)]

            for i in range(n):
                for k in range(1, max_k + 1):
                    if i == 0:
                        dp[i][k][0] = 0
                        dp[i][k][1] = -prices[0]
                        continue
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
            return dp[n - 1][max_k][0]

        def maxProfit2(self, k, prices):
            if not prices: return 0
            n = len(prices)
            if k >= n //2:
                return self.solutionT122_maxProfit(prices)

            dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
            for i in range(n):
                for x in range(1, k+1):
                    if i == 0:
                        dp[0][x][0] = 0
                        dp[0][x][1] = -prices[0]
                        continue
                    dp[i][x][0] = max(dp[i - 1][x][0], dp[i - 1][x][1] + prices[i])
                    dp[i][x][1] = max(dp[i - 1][x][1], dp[i - 1][x - 1][0] - prices[i])
            return dp[n - 1][k][0]

        def solutionT122_maxProfit(self, prices):
            n = len(prices)
            dp_i_0 = 0
            dp_i_1 = -float("inf")

            for i in range(n):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, tmp - prices[i])
            return dp_i_0


class Solution309(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])  # 这里当i=1时, i-2<0, 此时dp[-1][0]位置初始化正好为0
        return dp[n-1][0]

    def maxProfit2(self, prices):
        if not prices: return 0
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float("inf")
        dp_pre_0 = 0

        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp              # 注意cooldown变量的状态更新规则
        return dp_i_0


class SolutionT714(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

    def maxProfit2(self, prices, fee):
        if not prices: return 0
        n = len(prices)

        dp_i_0 = 0
        dp_i_1 = -float("inf")

        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0


if __name__ == '__main__':
    test = [7, 1, 5, 3, 6, 4]
    test2 = [3, 3, 5, 0, 0, 3, 1, 4]

    print(SolutionT121().maxProfit(test))
    print(SolutionT121().maxProfit2(test))

    print(SolutionT122().maxProfit(test))
    print(SolutionT122().maxProfit2(test))

    # print(SolutionT123().maxProfit(test))
    print(SolutionT123().maxProfit(test2))
