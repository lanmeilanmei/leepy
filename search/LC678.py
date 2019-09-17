"""
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True
注意:

字符串大小将在 [1，100] 范围内。
"""
# dfs 超时, 尚未看解析 https://zxi.mytechroad.com/blog/?s=Valid+Parenthesis+String


# unresolved
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = []
        self.dfs(s, 0, ans)
        for s in ans:
            if self.isValid(s): return True
        return False
        # return len(ans) > 0

    def dfs(self, S, i, ans):
        if i == len(S):
            # if self.isValid(S):
            ans.append(S)
            return

        self.dfs(S, i+1, ans)
        if S[i] == "*":
            tmp = S

            S = S[:i] + "(" + S[i+1:]
            self.dfs(S, i+1, ans)

            S = S[:i] + ")" + S[i + 1:]
            self.dfs(S, i + 1, ans)

            # S = S[:i] + "*" + S[i + 1:]
            # self.dfs(S, i + 1, ans)

            S = tmp

    def isValid(self, S):
        right, ct = 0, 0
        for i in range(len(S)-1, -1, -1):
            if S[i] == ")":
                right += 1
                ct += 1
            elif S[i] == "(":
                if right > 0:
                    right -= 1
                    ct -= 1
                else:
                    ct += 1
        return ct == 0

    def checkValidString_try(self, s):
        self.ans = False
        self.dfs_try(s, 0)
        return self.ans

    def dfs_try(self, S, i):
        if self.ans:
            return
        if i == len(S):
            if self.isValid(S):
                self.ans = True
            return

        self.dfs_try(S, i+1)
        if S[i] == "*" and not self.ans:
            tmp = S

            S = S[:i] + "(" + S[i + 1:]
            self.dfs_try(S, i + 1)

            if self.ans: return

            S = S[:i] + ")" + S[i + 1:]
            self.dfs_try(S, i + 1)

            S = tmp
