"""
856. 括号得分

递归法
存在三种字符串情况 "((()))"  "()()()"  "()(())"
重要的是，找到递归分裂点，再解决分数计算
time O(n^2)  space O(n)

拆解法
"(()(()))"   => "(())" + "((()))"
"(()(()()))" => "(())" + "((()))" + "((()))"
"""


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        return self.score(S, 0, len(S)-1)

    def score(self, s, left, right):
        if right - left == 1:   # 计算括号分数的基本情况 "()"
            return 1
        balance = 0
        for i in range(left, right):    # 由于是平衡括号组，令取不到最尾元素，进入第一种情况
            if s[i] == "(":
                balance += 1
            if s[i] == ")":
                balance -= 1
            if balance == 0:
                return self.score(s, left+1, i) + self.score(s, i+1, right)     # 第二、三种情况

        return 2 * self.score(s, left+1, right-1)

    def scoreOfParentheses2(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = 0
        deep = -1
        for i in range(len(S)):
            deep += 1 if S[i] == "(" else -1    # 前提: 整体是平衡括号
            if S[i] == "(" and S[i+1] == ")":
                ans += 1 << deep
        return ans
