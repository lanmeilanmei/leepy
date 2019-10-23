"""
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""
# 解法1, DP, 这里有两个状态影响因子, 以 nums[i] 结尾的最长升序序列的个数和长度. 分析如下:
# 在 nums[i] > nums[j] 时, 以 nums[i] 结尾的最长升序序列的长度更新方式是:
#   l[j] + 1 > l[i]   ====>  第一次找到以 nums[i] 结尾  l[i] = l[j] + 1  [加上自身]
# 在 nums[i] > nums[j] 时, 以 nums[i] 结尾的最长升序序列的个数有两种来源:
#   第一种, l[j] + 1 > l[i]   第一次找到以 nums[i] 结尾, c[i] = c[j] 个数保持不变 [注意此时长度有变, 因为考虑到 nums[i] 自身]
#   第二种, l[j] + 1 == l[i]  之前已经找到过 l[j] 的 nums[k], 此前 c[i] 记录的就是 c[k] 或初始化值, 因此更新为 c[i] += c[j]
# LC549

# 解法2 unresolved


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n: return 0

        c = [1] * n     # c[i] 记录以 nums[i] 结尾的最长升序序列的个数
        l = [1] * n     # l[i] 记录以 nums[i] 结尾的最长升序序列的长度

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        c[i] = c[j]
                    elif l[j] + 1 == l[i]:
                        c[i] += c[j]
        max_len = max(l)

        ans = 0
        for i in range(n):
            if l[i] == max_len:
                ans += c[i]
        return ans


if __name__ == '__main__':
    # print(Solution().findNumberOfLIS([1, 3, 5, 4, 7, 8]))

    print(Solution().findNumberOfLIS([1, 3, 5, 4, 7, 6, 5]))
