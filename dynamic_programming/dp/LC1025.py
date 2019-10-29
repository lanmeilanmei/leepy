"""
LC 1025 除数博弈

爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
 

提示：

1 <= N <= 1000
"""
# 解法1
# 记dp[N]为黑板上数字为N的情况下,Alice的输赢情况， 如果Alice取了数字x, 那么显然
# dp[N]与dp[N -x]输赢情况相反。x可以取的值很多，只要dp[N -xi]中任意一个为False, 那么dp[N]肯定为True, 否则dp[N]肯定为False

# 解法2
# 数学题: 偶数赢  奇数输


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = {}
        dp[1] = False
        dp[2] = True

        if N < 3:
            return dp[N]

        for i in range(3, N+1):
            dp[i] = False
            for j in range(1, i):
                if i % j == 0 and dp[i-j] == False:
                    dp[i] = True
                    break
        return dp[N]

    def divisorGame_2(self, N):
        return N % 2 == 0


if __name__ == '__main__':
    print(Solution().divisorGame(5))
