"""
746. 使用最小花费爬楼梯

数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# f(x) = min(f(x-1), f(x-2)) + cost[i]
# dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])


class Solutiont746(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [1000 * 1000] * n     # 已经提示长度和值最大都为1000, 这里没必要用sys.maxsize
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-1], dp[n-2])

    def minCostClimbingStairs_2(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]

    def minCostClimbingStairs_3(self, cost):
        dp1 = dp2 = 0
        for i in range(2, len(cost)+1):
            dp = min(dp1 + cost[i-1], dp2 + cost[i-2])
            dp2 = dp1
            dp1 = dp
        return dp1

    def minCostClimbingStairs_4(self, cost):
        def recursive(costs, m, i):
            if i < 0: return 0
            if m[i] > 0: return m[i]
            m[i] = min(recursive(costs, m, i - 1), recursive(costs, m, i - 2)) + costs[i]
            return m[i]

        n = len(cost)
        mm = [-1] * (n + 1)
        return min(recursive(cost, mm, n-1), recursive(cost, mm, n-2))


