"""
74. Search a 2D Matrix

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 解法1: O(m*log(n))
# 解法2：二维的一维表示法  Time complexity: O(log(m*n)) Time complexity: O(log(m*n))


# review
class SolutionT74(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        res = 0
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
               res = i
               break
        left, right = 0, len(matrix[res]) - 1
        while left < right:
            mid = left + (right - left) // 2
            if matrix[res][mid] == target: return True
            if matrix[res][mid] > target:
                right = mid
            else:
                left = mid + 1
        return True if matrix[res][left] == target else False

    def searchMatrix_2(self, matrix, target):
        if not matrix: return False
        left = 0
        cols = len(matrix[0])
        right = len(matrix) * len(cols)

        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            if matrix[mid // cols][mid % cols] > target:
                right = mid
            else:
                left = mid + 1

        return False
