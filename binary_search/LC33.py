"""
33. Search in Rotated Sorted Array 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# notes:
# 解法1，Time Complexity O(n), Space Complexity O(n) 有数组复制和重排序
# 解法2，Time Complexity O(n), Space Complexity O(1) 最差情况, 最后一个位置找到旋转点 Time Complexity O(n)
# 解法3 https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14629/Python-O(lgn)-solution-(It-needs-a-pen-and-some-paper-to-figure-it-out-at-the-first-time).
# 解法4 与模板的细节一致 Time Complexity O(logn), Space Complexity O(1)


class SolutionT33(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bianry_search(ls, left, right):
            while left < right:
                mid = left + (right - left) // 2
                if ls[mid] == target: return mid
                if ls[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return -1

        sorted_nums = sorted(nums)
        i = bianry_search(sorted_nums, 0, len(nums))

        if i == -1: return -1
        return nums.index(sorted_nums[i])

    def search_2(self, nums, target):
        def bianry_search(ls, left, right):
            while left < right:
                mid = left + (right - left) // 2
                if ls[mid] == target: return mid
                if ls[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return -1

        def search_split(ls, n):
            k = 0
            for i in range(1, n):
                if ls[i] < ls[i-1]:
                    k = i
                    break
            return k

        N = len(nums)
        i = search_split(nums, N)
        if i == 0: return bianry_search(nums, 0, N)
        if target == nums[i]: return i
        if target > nums[i-1]:                          # 先判断边界
            return -1
        elif target > nums[-1]:                         # 再判断单侧范围
            return bianry_search(nums, 0, i)
        else:
            return bianry_search(nums, i+1, N)

    def search_3(self, nums, target):
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search_4(self, nums, target):
        if not nums: return -1
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] < nums[mid]:                  # 左侧有序，已经去重不用考虑=
                if nums[left] <= target < nums[mid]:    # 判断目标是否在左侧范围
                    right = mid
                else:
                    left = mid + 1                      # 若不在左半区，则跳到右半区
            else:                                       # 右侧有序
                if nums[mid] < target <= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid
        return -1
