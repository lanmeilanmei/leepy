"""
1130. 叶值的最小代价生成树
"""
# 解法1 DP 代价状态方程 unresolved


class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        # dp[i][j] 表示 arr 数组中第i个元素到第j个元素构成树所需的最小代价
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        # maxval[i][j] 存储子数组 arr[i: j+1] 的最大值
        maxval = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                maxval[i][j] = max(arr[i: j+1])
        # 单结点代价初始为0
        for i in range(n):
            dp[i][i] = 0

        for window in (1, n): # 可比较的代价窗口大小
            for start in range(n-window): # 可比较的起始位置
                for k in range(start, start+window): # 计算代价切分左右子树的位置
                    dp[start][start+window] = min(
                        dp[start][start+window],
                        dp[start][k] + dp[k+1][start+window] + maxval[start][k] * maxval[k+1][start+window]
                    )

        return dp[0][n-1]


if __name__ == '__main__':
    print(Solution().mctFromLeafValues([6, 2, 4]))

