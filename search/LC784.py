"""
784. 字母大小写全排列
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。
"""
# 此题是 "同一位置多种可能的" & "排列搜索" 问题的解题模板
# 注意 "同一位置多种可能的" 的 dfs 执行顺序
# lc46: 不重复元素全排列
# lc47: 重复元素去重全排列
# lc784: 单点位多可能性的全排列


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(S, 0, ans)
        return ans

    def dfs(self, S, start, ans):
        if start == len(S):
            ans.append(S)
            return

        self.dfs(S, start+1, ans)       # 这里的dfs是保证每一种可能性被成功添加
        if S[start].isalpha():
            S = self.convert(S, start)  # 转换字母
            self.dfs(S, start+1, ans)
            S = self.convert(S, start)  # 恢复

    def convert(self, S, i):
        tmp = ""
        for j in range(len(S)):
            c = S[j]
            if i == j:
                c = chr(ord(c) ^ 32)
            tmp += c
        S = tmp
        return S

