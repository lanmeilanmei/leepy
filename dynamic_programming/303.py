"""
303. Range Sum Query - Immutable 303. 区域和检索 - 数组不可变

给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 最优解公式：当前累加和 = 当前值 + 之前累加和
# Time complexity: pre-compute: O(n), query: O(1), Space complexity: O(n)
# 这里如果用api解决多次查询耗时较大


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums: return
        self.sums = nums[:]
        for i in range(1, len(nums)):
            self.sums[i] += self.sums[i-1]      # DP，记忆化递归，最优公式：当前累加和 = 当前值 + 之前累加和

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if  i== 0: return self.sums[j]
        return self.sums[j] - self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
