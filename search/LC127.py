"""
127. 单词接龙

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
"""
# 解法1的dfs未能解决
# 单向BFS、双向BFS, 图, BFS模板
# https://leetcode-cn.com/problems/word-ladder/solution/dan-ci-jie-long-by-leetcode/


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def find_similar(word):
            word = set(list(word))
            return [wo for wo in wordList if len(word - set(list(wo))) == 1]

        def dfs(S, used, cts, ans):
            if S == endWord:
                ans.append(cts)
                return

            for candi in wordDict[S]:
                if used[candi]: continue
                used[candi] = True
                cts.append(candi)
                dfs(candi, used, cts, ans)
                cts.pop()
                used[candi] = False

        wordDict = {}
        used = {}
        for w in wordList + [beginWord]:
            if w == beginWord:
                used[w] = True
            else:
                used[w] = False
            wordDict[w] = find_similar(w)

        ans = []
        dfs(beginWord, used, [beginWord], ans)
        # return min(ans) if ans else 0
        return ans

    def ladderLength_official_BFS(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.pop()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))

                all_combo_dict[intermediate_word] = []
        return 0


from collections import defaultdict


class Solution2(object):
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            for word in self.all_combo_dict[intermediate_word]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        while queue_begin and queue_end:

            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


if __name__ == '__main__':

    # print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    #
    # print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

    # print(Solution().ladderLength("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"]))

    # print(Solution().ladderLength_official_BFS("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

    # print(Solution().ladderLength_official_BFS("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"]))

    print(Solution2().ladderLength("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"]))
