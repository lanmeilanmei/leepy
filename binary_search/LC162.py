"""
162. Find Peak Element

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# https://leetcode.com/problems/find-peak-element/discuss/50367/Python-iterative-and-recursive-solutions.


# review
class SolutionT162(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
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

    def findPeakElement_2(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

    def findPeakElement_3(self, nums):
        return self.binary_search(nums, 0, len(nums)-1)

    def binary_search(self, nums, left, right):
        if left == right:
            return left

        mid = left + (right - left) // 2
        if nums[mid] > nums[mid+1]:
            return self.binary_search(nums, left, mid)
        else:
            return self.binary_search(nums, mid+1, right)

    def findPeakElement_4(self, nums):
        if not nums: return 0
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if (mid - 1 < 0 or nums[mid-1] < nums[mid]) and nums[mid] > nums[mid+1]:    # 双数列表会返回左侧，因此mid+1始终可用
                return mid
            elif nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left     # left == right
