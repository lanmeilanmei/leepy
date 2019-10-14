# unresolved
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

    def ladderLength_official_BFS2(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        self.length = len(beginWord)
        self.all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)



    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            pass


if __name__ == '__main__':

    # print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    #
    # print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

    # print(Solution().ladderLength("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"]))

    # print(Solution().ladderLength_official_BFS("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

    print(Solution().ladderLength_official_BFS("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"]))
