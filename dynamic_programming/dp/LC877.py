"""
LC877 石头游戏
"""
# 解法1 记忆化递归 LTE
# https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-by-leetcode/

# 解法2 数学问题, 偶数堆时总是先手赢


# review
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        def dfs(left, right):
            if left > right:
                return 0

            first = (right - left - N) % 2
            if first == 1:
                return max(piles[left] + dfs(left+1, right), piles[right] + dfs(left, right-1))
            else:
                return min(-piles[left] + dfs(left+1, right), -piles[right] + dfs(left, right-1))

        N = len(piles)

        return dfs(0, N-1) > 0

    def stoneGame_2(self, piles):
        return True
