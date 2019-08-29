"""
852. Peak Index in a Mountain Array

我们把符合下列属性的数组 A 称作山脉：

A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

示例 1：

输入：[0,1,0]
输出：1
示例 2：

输入：[0,2,1,0]
输出：1
 

提示：

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A 是如上定义的山脉

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# https://leetcode.com/problems/find-peak-element/discuss/50367/Python-iterative-and-recursive-solutions.


# review with 162、153、154、33、34
class SolutionT852(object):
    def peakIndexInMountainArray(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0                                     # 初始化防单元素列表
        for i in range(1, len(nums)):
            if i + 1 < len(nums):
                if nums[i-1] < nums[i] > nums[i+1]:
                    res = i
                    break
            else:
                if nums[i - 1] < nums[i]:
                    res = i
                    break
        return res

    def peakIndexInMountainArray_2(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

    def peakIndexInMountainArray_3(self, nums):
        return self.binary_search(nums, 0, len(nums)-1)

    def binary_search(self, nums, left, right):
        if left == right:
            return left

        mid = left + (right - left) // 2

        if nums[mid] > nums[mid+1]:
            return self.binary_search(nums, left, mid)
        else:
            return self.binary_search(nums, mid+1, right)

    def peakIndexInMountainArray_4(self, nums):
        if not nums: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if (mid - 1 < 0 or nums[mid-1] < nums[mid]) and nums[mid] > nums[mid+1]: # (单元素 or 升序) and 降序
                return mid
            elif nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
