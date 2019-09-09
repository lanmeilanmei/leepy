"""
39. Combination Sum 组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
# 组合搜索问题, 但是允许元素多次有序重复组合


class SolutionT39(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, candidates, target, start, path, ans):
        if target == 0:
            ans.append(path[:])
            return

        for i in range(start, len(candidates)):         # start与i值搭配, 可重复选取组合数
            if candidates[i] > target: break            # 由于待选数是有序的, 这里提前剪枝
            path.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, path, ans)
            path.pop()

    # 按结果数组的长度顺序返回, [[7], [2, 2, 3]]
    def combinationSum_order(self, candidates, target):
        ans = []
        candidates.sort()
        for i in range(1, target // candidates[0] + 1):
            self.dfs_order(candidates, target, 0, 0, i, [], ans)
        return ans

    def dfs_order(self, candidates, target, start, depth, n, path, ans):
        if depth == n:
            if target == 0:
                ans.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target: break
            path.append(candidates[i])
            # 这里start位置如果重复传入start, 返回结果有重复, 传入i保证后续元素都是在start索引后的元素
            self.dfs_order(candidates, target-candidates[i], i, depth+1, n, path, ans)
            path.pop()
