"""
377. Combination Sum IV 组合总和 Ⅳ

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？
"""
# 这题组合搜索模板可以解决, 但是超时, 此时需要进阶到DP优化递归
# 39、40、216. 注意比较dfs中循环调用dfs的i和start的返回区别!!!


class SolutionT377(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = []
        nums.sort()
        self.dfs(nums, target, 0, [], ans)
        return len(ans)

    def dfs(self, nums, target, start, path, ans):
        if target == 0:
            if path not in ans:
                ans.append(path[:])
            return

        for i in range(start, len(nums)):         # start与i值搭配, 可重复选取组合数
            if nums[i] > target: break            # 由于待选数是有序的, 这里提前剪枝
            path.append(nums[i])
            self.dfs(nums, target-nums[i], start, path, ans)    # 注意这里是start,可"无序"返回所有结果.不同于LC39、LC40
            path.pop()
