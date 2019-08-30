"""
378. Kth Smallest Element in a Sorted Matrix

给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
说明:
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# TODO unresolved
class SolutionT378(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def upper_bound(nums, val, left, right):
            """
            查找第一个大于目标数的元素
            如果目标数比该行尾元素大，则返回该行个数，如果目标数比首元素小，则返回0
            """
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > val:
                    right = mid
                else:
                    left = mid + 1
            return left

        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1] + 1

        while left < right:
            mid = left + (right - left) // 2
            ct = 0
            for i in range(n):
                ct += upper_bound(matrix[i][0], matrix[i][-1], mid)
                pass




