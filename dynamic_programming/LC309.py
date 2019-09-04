"""
309. Best Time to Buy and Sell Stock with Cooldown 最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""

""" 
    假设冷冻期状态为rest, 买进和卖出之间的状态为hold, 持有和冷冻期之间的瞬态为sold, 则有如下状态转移方程(最好在纸上表示):
        rest[自循环]  ====buy===>>  hold[自循环] ====sell===>> (sold) ===rest===>> rest[自循环]
    
    则可知: 
        hold[i] = max(hold[i-1], rest[i-1] - prices[i])  第i天继续持有的金额 和 第i天从冷冻期终结而买入后最后的金额 的较大者
        sold[i] = hold[i-1] + prices[i]
        rest[i] = max(rest[i-1], sold[i-1])
    
    需要初始化 rest[0] = sold[0] = 0, hold[0] = 负无穷
    ans = max(rest[i], sold[i])
    Time Complexity: O(n) , Space Complexity: O(n) -> O(1) [滚动数组]
"""


# review
class SolutionT309(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        hold = -sys.maxsize
        rest = sold = 0
        for price in prices:
            pre_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, pre_sold)
        return max(rest, sold)
