"""
72. 编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
# 解法1: 记忆化递归, 没有理解太多题意. 按照题目给的条件去写对三种操作即可.
# 对于记忆数组dp的初始化, 有word1和word2的影响, 双方每一个位置都可能发生变化. 因此初始化为二维数组.
# 解法2: 滚动数组, 初始化但需要设置边界情况.
# time complexity: O(l1 * l2),  space complexity: O(l1 * l2)
# 记忆化递归、DP 写法模板


# review
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def minDistance(w1, w2, ll1, ll2):
            if ll1 == 0:
                return ll2
            if ll2 == 0:
                return ll1

            if dp[ll1][ll2] >= 0:
                return dp[ll1][ll2]

            ans = 0
            if w1[ll1 - 1] == w2[ll2 - 1]:  # 最后一位相同
                ans = minDistance(w1, w2, ll1 - 1, ll2 - 1) # 这里不是替换, 是给出剩下位置的距离. 代码和替换一样, 但是ans=0
            else:
                a = minDistance(w1, w2, ll1 - 1, ll2 - 1)   # 替换
                b = minDistance(w1, w2, ll1 - 1, ll2)       # 删除
                c = minDistance(w1, w2, ll1, ll2 - 1)       # 插入
                ans = min(a, min(b, c)) + 1
            dp[ll1][ll2] = ans
            return ans

        l1 = len(word1)
        l2 = len(word2)

        dp = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]
        return minDistance(word1, word2, l1, l2)

    def minDistance_dp(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        for i in range(l1+1):
            dp[i][0] = i        # word2为空串, word1需要修改i步
        for j in range(l2+1):
            dp[0][j] = j        # word1为空串, word2需要修改j步

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                c = 0 if word1[i-1] == word2[j-1] else 1    #
                dp[i][j] = min(dp[i-1][j-1] + c, min(dp[i][j-1], dp[i-1][j]) + 1)
        return dp[l1][l2]


if __name__ == '__main__':
    print(Solution().minDistance("abbc", "acc"))

    print(Solution().minDistance_dp("abbc", "acc"))

    print(Solution().minDistance("horse", "ros"))

    print(Solution().minDistance("intention", "execution"))
