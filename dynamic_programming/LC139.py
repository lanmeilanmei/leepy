"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
# dfs, 时间复杂度：O(n^n), 空间复杂度：O(n)
# 记忆化dfs, 时间复杂度：O(n^2), 空间复杂度：O(n)


# need review
class Solution(object):
    # dfs, Time Limit Exceeded
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def dfs(s, wordSet, start):
            if start == len(s):     # 边界
                return True

            for i in range(start+1, len(s)+1):  # 边界
                if s[start:i] in wordSet and dfs(s, wordDict, i):   # 分割word, 检查
                    return True

            return False    # 所有粒度的分割检查失败后, 返回False

        return dfs(s, set(wordDict), 0)

    # dfs with memo, Time Limit Exceeded, 应该是个假的
    def wordBreak2(self, s, wordDict):
        def dfs(S, wordSet, start, memo):
            if start == len(S):
                return True

            if memo[start]:
                return memo[start]

            for i in range(start+1, len(S)+1):
                if s[start:i] in wordSet and dfs(S, wordSet, i, memo):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(s, set(wordDict), 0, [False] * len(s))

    def wordBreak3(self, s, wordDict):
        wordSet = set(wordDict)
        queue = [0]
        visited = [0] * len(s)

        while queue:
            start = queue.pop()
            if visited[start] == 0:
                for end in range(start+1, len(s)+1):
                    if s[start: end] in wordSet:
                        queue.append(end)
                        if end == len(s):
                            return True

                visited[start] = 1

        return False

    # dfs with memo
    def wordBreak_hh(self, s, wordDict):
        def canBreak(S, memo, wordSet):
            if S in memo:
                return memo[S]
            if S in wordSet:
                memo[S] = True
                return True

            for i in range(1, len(S)):
                word = S[i:]
                if word in wordDict and canBreak(S[0: i], memo, wordSet):
                    memo[S] = True
                    return True

            memo[S] = False
            return False

        return canBreak(s, {}, set(wordDict))

    def wordBreak_ckh(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True

        for end in range(1, len(s)+1):
            for start in range(end):
                # print(dp[start], start, end, "--->", s[start: end])
                if dp[start] and s[start: end] in wordDict:
                    dp[end] = True  # 标记 end 处是打卡点,且从end 位置开始可进行再分割
                    break
            # print("----------")
        return dp[-1]


if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict))

    print(Solution().wordBreak2("bb", ["a", "b", "bbb", "bbbb"]))

    print(Solution().wordBreak3("bb", ["a", "b", "bbb", "bbbb"]))

    # print(Solution().wordBreak_ckh(s, wordDict))

    print(Solution().wordBreak_ckh("catsandog", ["cats", "dog", "sand", "and", "cat"]))
