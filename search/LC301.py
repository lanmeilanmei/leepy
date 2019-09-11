"""
301. 删除无效的括号
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]
"""
# "括号约束"组合搜索模板, 注意与lc39 lc40的差别比较
# 组合搜索问题, 就是在给定了明确的搜索空间内进行有剪枝的伪穷举搜索
# 所以dfs搜索需要明确两点:  搜索条件(继续下一次dfs或结束)、搜索边界(添加可能的结果或结束)

# 这一题要求返回删除无效括号后的有效组合结果, 首先要得到无效的左右括号个数
# 此时组合搜索就是对已有的左右括号个数限制下进行搜索, 最后对每一个结果进行有效判定
# 搜索条件和搜索边界有时容易混合
# 在这里搜索条件, 理解为 s[i] in "()" + left/right > 0 为多次dfs的充要条件
# 而搜索边界则是 left == right == 0, 满足时则停止当前局部dfs搜索, 如果isValid(s), 则添加到结果集

# DP解法暂未解锁


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1
            if c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1

        ans = []
        self.dfs(s, 0, left, right, ans)
        return ans

    def dfs(self, s, start, left, right, ans):
        if left == right == 0:
            if self.isValid(s):
                ans.append(s)
            return

        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]: continue   # 保证连续重复元素仅有前者可被使用
            if s[i] in "()":
                tmp = s[:i] + s[i+1:]
                if right > 0 and s[i] == ")":               # 这里先判断左或右无区别
                    self.dfs(tmp, i, left, right-1, ans)
                elif left > 0 and s[i] == "(":
                    self.dfs(tmp, i, left-1, right, ans)

    def isValid(self, s):
        ct = 0
        for c in s:
            if c == "(": ct += 1
            if c == ")": ct -= 1
            if ct < 0:
                return False
        return True


