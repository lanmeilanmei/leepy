"""
943. 最短超级串

给定一个字符串数组 A，找到以 A 中每个字符串作为子字符串的最短字符串。

我们可以假设 A 中没有字符串是 A 中另一个字符串的子字符串。

示例 1：

输入：["alex","loves","leetcode"]
输出："alexlovesleetcode"
解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
示例 2：

输入：["catg","ctaagt","gcta","ttca","atgcatc"]
输出："gctaagttcatgcatc"
 

提示：

1 <= A.length <= 12
1 <= A[i].length <= 20
"""
# dfs搜索会超时，但是是dfs排列搜索的高阶模板


class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        minStr = "".join(A)
        ans = [minStr]
        self.dfs(A, 0, len(A), [False] * len(A), "", ans)
        return ans[0]

    def dfs(self, strList, depth, n, used, pathStr, ans):
        if len(pathStr) > len(ans[0]): return
        if depth == n:
            ans[0] = pathStr
            return

        for i in range(len(strList)):
            if used[i] is True: continue
            used[i] = True

            pre = pathStr
            if strList[i] in pathStr:
                self.dfs(strList, depth+1, n, used, pathStr, ans)
            else:
                j = self.getTailSameStrIndex(pathStr, strList[i])
                pathStr += strList[i][j:]
                self.dfs(strList, depth+1, n, used, pathStr, ans)
            pathStr = pre
            used[i] = False

    # 最长尾部连续公共子字符串
    def getTailSameStrIndex(self, pathStr, strElem):
        j = 0
        for i in range(len(strElem)):
            if pathStr[-(i+1):] == strElem[:i+1]:
                j = i + 1
        return j

    # 最长尾部连续公共子字符串
    def getTailSameStrIndex_2(self, pathStr, strElem):
        for i in range(len(pathStr)):
            if strElem.startswith(pathStr[i:]):
                return len(pathStr) - i
        return 0

    def getDistance(self, s1, s2):
        for i in range(1, len(s1)):
            if s2.startswith(s1[i:]):
                return len(s1) - i
        return 0

    def path2Str(self, A, G, path):
        res = A[path[0]]
        for i in range(1, len(path)):
            indice = G[path[i-1]][path[i]]
            res += A[path[i]][indice:]
        return res

    def shortestSuperstring_DP(self, A):
        # 先构造图
        n = len(A)
        G = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                G[i][j] = self.getDistance(A[i], A[j])
                G[j][i] = self.getDistance(A[j], A[i])

        import collections
        d = [[0] * n for _ in range(1 << n)]
        Q = collections.deque([(i, 1 << i, [i], 0) for i in range(n)])
        l = -1  # 记录最大的repeat_len   表示目前重复部分的长度
        P = []  # 记录对应的path
        while Q:
            node, mask, path, dis = Q.popleft()
            if dis < d[mask][node]: continue
            if mask == (1 << n) - 1 and dis > l:
                P, l = path, dis
                continue
            for i in range(n):
                nex_mask = mask | (1 << i)
                # case1: 不能走回头路，因为每个结点只能遍历一次
                # case2: 如果走当前这条路能够获得更大的重复长度，才继续考虑
                if nex_mask != mask and d[mask][node] + G[node][i] >= d[nex_mask][i]:
                    d[nex_mask][i] = d[mask][node] + G[node][i]
                    Q.append((i, nex_mask, path + [i], d[nex_mask][i]))

        return self.path2Str(A, G, P)
