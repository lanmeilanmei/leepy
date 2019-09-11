"""
22. 括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# "括号约束"组合搜索模板

# 这里每个位置都有两种选择进行组合, 但同时又有全局约束.
# 注意与 lc784 的局部位置多可能性的"排列搜索"问题比较
# 剪枝条件的写法上, 第二种方法更为清晰


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.dfs(n, n, "", ans)
        return ans

    def dfs(self, left, right, path, ans):
        if left + right == 0:
            ans.append(path)
            return

        if right < left: return        # 这是剩余数量, right<left说明此时path中左右括号数量相等
        if left > 0:
            path += "("
            self.dfs(left-1, right, path, ans)
            path = path[:-1]
        if right > 0:
            path += ")"
            self.dfs(left, right-1, path, ans)
            path = path[:-1]

    def generateParenthesis_2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs_2("", n, 0, 0, res)
        return res

    def dfs_2(self, S, n, left, right, res):
        if len(S) == 2 * n:
            res.append(S)
            return

        if left < n:
            self.dfs_2(S + "(", n, left + 1, right, res)
        if right < left:                                    # 组成合法括号的充分条件
            self.dfs_2(S + ")", n, left, right + 1, res)
