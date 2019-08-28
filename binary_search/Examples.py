"""
这里是根据 notes 文件引出的例子
"""


class SolutionEx(object):
    def binary_search_01(self, A, val, left, right):
        """
        返回给定值在有序数组中的index,数组元素唯一。未找到则返回-1  [要求已排序]
        """
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] == val: return mid        # f(m)
            if A[mid] > val:                    # g(m)
                right = mid
            else:
                left = mid + 1
        return -1

    def lower_bound(self, A, val, left, right):
        """
        返回某数在有序数组中的下界index  [要求已排序]
        """
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] >= val:                   # g(m), 因为f(m)不一定有
                right = mid
            else:
                left = mid + 1
        return left

    def upper_bound(self, A, val, left, right):
        """
        返回某数在有序数组中的上界index  [要求已排序]
        """
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] > val:
                right = mid
            else:
                left = mid + 1
        return left

    def sqrt(self, x):
        """
        求最接近sqrt(x)的数，这里与upper_bound类似，都是求不超过目标值的最大值
        """
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:                   # 这里g(m)比上面略复杂
                right = mid
            else:
                left = mid + 1
        return left - 1

    def firstBadVersion(self, n):
        def isBadVersion(x):
            return

        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):               # g(m)比上面略复杂
                right = mid
            else:
                left = mid + 1
        return left
