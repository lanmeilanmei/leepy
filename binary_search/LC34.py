"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
# 解法1： 就是模板中上下界的求法 Time complexity: O(logn) Space complexity: O(1)
# 解法2： 根据lower_bound先求下届，再探索上界


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lower_bound(A, val, left, right):
            exist = False
            while left < right:
                mid = left + (right - left) // 2
                if A[mid] == val: exist = True
                if A[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return left if exist else -1

        def upper_bound(A, val, left, right):
            exist = False
            while left < right:
                mid = left + (right - left) // 2
                if A[mid] == val: exist = True
                if A[mid] > val:
                    right = mid
                else:
                    left = mid + 1
            return left-1 if exist else -1

        N = len(nums)
        return [lower_bound(nums, target, 0, N), upper_bound(nums, target, 0, N)]

    def searchRange_2(self, nums, target):
        def lower_bound(A, val, left, right):
            exist = False
            while left < right:
                mid = left + (right - left) // 2
                if A[mid] == val: exist = True
                if A[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return left if exist else -1

        N = len(nums)
        le = lower_bound(nums, target, 0, N)
        if le == -1: return [-1, -1]

        ri = le
        for i in range(le, N):
            if nums[i] == nums[le]:
                ri = i
            else:
                break
        return [le, ri]
