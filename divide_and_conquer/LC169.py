"""

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def divide_and_conquer(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = divide_and_conquer(lo, mid)
            right = divide_and_conquer(mid + 1, hi)

            if left == right:
                return left

            left_count = sum([1 for i in range(lo, hi + 1) if nums[i] == left])
            right_count = sum([1 for i in range(lo, hi + 1) if nums[i] == right])

            return left if left_count > right_count else right

        return divide_and_conquer(0, len(nums) - 1)


test1 = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(test1))
