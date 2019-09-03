"""
121. Best Time to Buy and Sell Stock 买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
# 穷举法超时, 这里主要讲DP思路
# 最大利润定义, 一次买进一次卖出, 卖出在买进行为之后
# max_profit = max(price[j] - price[i]), 0 <= i < j <= n-1
# 也就是说在第k天时, 第k天之前的极小值为price[i], 第k天及以后的极大值是price[j]
# 解法1: 维护两个数组, 在第i天前的最低价格数组lowest, 在第i天时的目前最大利润数组most
# 解法1: 最大利润数组是由  第i天前最大利润  和 第i天决定卖出 的较大者生成
# 解法1: Time Complexity O(n), Space Complexity O(n)
# 解法1的滚动数组解法形式 Space Complexity O(1)

# 解法2: 直接将连续收益给出, 得到连续持仓的收益状态公式 gains[i-1] = prices[i] - prices[i-1]
# 解法2: 得到连续持仓的收益序列后, 应用 LC53中的最大子序和即可
# 解法2: Time Complexity O(n) + O(n), Space Complexity O(n)


# review
class SolutionT121(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        lowest = prices[:]
        most = [-prices[0]] * n
        for i in range(1, n):
            lowest[i] = min(lowest[i-1], prices[i])             # 状态转移公式
            most[i] = max(most[i-1], prices[i] - lowest[i])     # 状态转移公式

        return most[n-1] if most[n-1] > 0 else 0

    # 解法1, cp from hh
    def maxProfit_hh(self, prices):
        if not prices: return 0
        n = len(prices)
        lowest = [prices[0]] * n
        most = [0] * n
        for i in range(1, n):
            lowest[i] = min(lowest[i-1], prices[i])
            most[i] = max(most[i-1], prices[i] - lowest[i-1])
        return most[n-1]

    # 解法1思路的滚动数组
    def maxProfit_hh_roll(self, prices):
        if not prices: return 0
        n = len(prices)
        lowest = prices[0]
        most = 0
        for i in range(1, n):
            lowest = min(lowest, prices[i])            # 如果most公式提前,则表示不可以当天卖出,更准确
            most = max(most, prices[i] - lowest)       # 这里写法和最上面lowest有区别, 可以在当天卖出
        return most

    def maxProfit_consistent(self, prices):
        n = len(prices)
        if n < 2: return 0                              # 一个元素返回0，上面也可以这么写
        gains = [0] * (n-1)
        for i in range(1, n):
            gains[i-1] = prices[i] - prices[i-1]        # 连续持仓的收益状态公式
        return max(0, self.__helper(gains))

    def __helper(self, nums):                           # LC53 最大连续子序和
        n = len(nums)
        f = [nums[0]] * n
        for i in range(1, n):
            f[i] = max(f[i-1] + nums[i], nums[i])
        return max(f)
