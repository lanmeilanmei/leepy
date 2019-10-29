"""
392. 判断子序列

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""
# 解法1 常规思路 O(n)
#


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        si = 0
        sl = len(s)
        tl = len(t)
        for i in range(tl):
            if s[si] == t[i]:
                si += 1
            if si == sl:
                return True
        return False

    def isSubsequence_2(self, s, t):
        dp = [[-1]] * 26
        tag = -1

        # 存储各个字母出现的位置序号
        for i in range(len(t)):
            p = ord(t[i]) - ord("a")
            dp[p].append(i)

        for i in range(len(s)):
            now = ord(s[i]) - ord("a")
            left = 0
            right = len(dp[now]) - 1

            while left < right:
                mid = (left + right) // 2
                if dp[now][mid] > tag:
                    right = mid
                else:
                    left = mid + 1

            if right < left or dp[now][left] == tag:
                return False
            tag = dp[now][left]

        return True


if __name__ == '__main__':
    print(Solution().isSubsequence("abc", "ahbgdc"))

    print(Solution().isSubsequence_2("abc", "ahbgdc"))

    print(Solution().isSubsequence("axc", "ahbgdc"))

    print(Solution().isSubsequence_2("axc", "ahbgdc"))
