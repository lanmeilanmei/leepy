"""
40. Combination Sum II 组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""
# 组合搜索问题, 一次取数


class SolutionT40(object):
    def combinationSum2(self, candidates, target):
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
            # if path not in ans:                           # 这里和下面的continue语句都可以避免重复
            ans.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target: break
            if i > start and candidates[i] == candidates[i-1]: continue # 提前剪枝, 由于原数组升序可避免重复
            path.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, path, ans)
            path.pop()
