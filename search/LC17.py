"""
17. Letter Combinations of a Phone Number 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
# 经典的组合搜索问题, DFS 或 BFS.  也是一种隐式的图搜索问题: "2" -> "3" 只有a、b、c三条边
# Time Complexity: O(4^n), n是输入的长度, Space Complexity: O(4^n + n)
# Time Complexity: O(4^n), n是输入的长度, Space Complexity: O(2 * 4^n)


class SolutionT17(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        curr = [' ' for _ in range(len(digits))]
        ans = []
        self.dfs(digits, d, 0, curr, ans)
        return ans

    def dfs(self, digits, dic, index, curr, ans):
        if index == len(digits):
            if index > 0:                       # 这里是防止Py负索引问题
                ans.append("".join(curr))
            return

        for c in dic[int(digits[index])]:
            curr[index] = c  # 这里dfs的中间结果本应该是str, 这里用list装载, 阔以用index重新复制, 正好省去dfs过程中字符串尾部的删除再添加或 s+c的临时创建操作
            self.dfs(digits, dic, index+1, curr, ans)

    def letterCombinations_BFS(self, digits):
        if not digits: return []
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []                # BFS标准模板, tmp在内、外层循环中间
            for s in ans:           # 每个输入都会"访问"结果容器 ans
                for c in d[int(digit)]:
                    tmp.append(s+c)         # 每个输入"访问"结果容器的最终形式
            ans = tmp               # 更新当前结果容器, BFS思想
        return ans
