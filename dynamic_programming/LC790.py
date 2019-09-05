"""
790. Domino and Tromino Tiling 多米诺和托米诺平铺

有两种形状的瓷砖：一种是 2x1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

XX  <- 多米诺

XX  <- "L" 托米诺
X
给定 N 的值，有多少种方法可以平铺 2 x N 的面板？返回值 mod 10^9 + 7。

（平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）

示例:
输入: 3
输出: 5
解释:
下面列出了五种不同的方法，不同字母代表不同瓷砖：
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
提示：

N  的范围是 [1, 1000]
"""
# 状态转移公式  dp[i] = (dp[i-3] + 2 * dp[i-1]) % kMod
# 详细见视频 https://www.bilibili.com/video/av31373698, 由单例规律到多例组合规律
# 这题既然出自周赛, 短时间内真的能就瓷砖的三种临时状态做瞬态分析吗
# 周赛最直接的反应应该还是根据个例来归纳出最终的最优状态公式吧


# review
class SolutionT790(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        kMod = 10 ** 9 + 7
        dp = [1] * (N+1)
        if N < 2: return dp[N]
        dp[2] = 2                   # 这里还有初始化 dp[0] = dp[1] = 1
        for i in range(3, N+1):
            dp[i] = (dp[i-3] + 2 * dp[i-1]) % kMod
        return dp[N]
