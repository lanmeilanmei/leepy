"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""
# Time complexity: O(2^n), Space complexity: O(2^n)


# view again !
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def dfs(S, wordSet, memo):
            if S in memo:
                return memo[S]

            ans = []
            if S in wordSet:
                ans.append(S)

            for i in range(1, len(S)):  # 这里初始索引从1开始是合理的, dfs初始进来会检查 if S in memo
                right = S[i:]
                if right in wordSet:
                    for w in dfs(S[0:i], wordSet, memo):
                        ans += [w + " " + right]

            memo[S] = ans
            return memo[S]

        return dfs(s, set(wordDict), {})


if __name__ == '__main__':
    # print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

