"""
153. Find Minimum in Rotated Sorted Array

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 解法2： 类似LC33 LC81  关键是找到有序数组的旋转点，旋转点位置即最小元素
# 解法3： 模板 需要注意的是，需要判断nums[right]时，切换成左右闭区间比较合适
# 解法4：http://zxi.mytechroad.com/blog/leetcode/leetcode-153-find-minimum-in-rotated-sorted-array/


# TODO
class Solutiont153(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                res = i
                break
        return nums[res]

    def findMin_2(self, nums):
        N = len(nums)
        left, right = 0, N
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid-1]:
                if mid + 1 >= N: return nums[mid]               # 两个元素
                if nums[mid] < nums[mid+1]: return nums[mid]    # 多于两个元素
            if nums[mid] > nums[left]:                          # 在旋转点的左边，已经去重，无需考虑=
                if nums[mid] <= nums[right-1]:                  # 全局有序，直接取最左端即可
                    return nums[left]
                else:                                           # 在旋转点的右边
                    left = mid + 1
            else:
                right = mid
        return nums[left]                                       # 这里最终返回是盲写，对[1]单元素测试有效

    def findMin_3(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMin_4(self, nums):
        return self.binary_search(nums, 0, len(nums)-1)

    def binary_search(self, nums, left, right):
        if left + 1 >= right:
            return min(nums[left], nums[right])

        if nums[left] < nums[right]:
            return nums[left]

        mid = left + (right - left) // 2

        return min(self.binary_search(nums, left, mid-1), self.binary_search(nums, mid, right))
