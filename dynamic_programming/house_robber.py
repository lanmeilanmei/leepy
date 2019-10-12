"""
house robber 专栏
198、213、337
"""


class SolutionT198(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = nums[0]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][0], dp[i - 2][1] + nums[i], dp[i - 2][0] + nums[i])
        return max(dp[n - 1][0], dp[n - 1][1])

    def rob2(self, nums):
        if not nums: return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp_i_0 = 0
        dp_i_1 = 0
        dp_pre_0 = 0
        dp_pre_1 = 0

        for i in range(n):
            tmp_0 = dp_i_0
            tmp_1 = dp_i_1
            dp_i_0 = max(dp_i_0, dp_i_1)
            dp_i_1 = max(dp_i_0, dp_pre_1 + nums[i], dp_pre_0 + nums[i])
            dp_pre_0 = tmp_0
            dp_pre_1 = tmp_1
        # return max(dp_i_0, dp_i_1)
        return dp_i_1

    def rob3(self, nums):
        """ 上面是按照各个影响变量拆分状态, 这里按照当前房间的最大累计金钱进一步简化rob2 """
        if not nums: return 0
        n = len(nums)
        if n < 2:
            return max(nums)
        dp_pre = 0
        dp_i = 0

        for i in range(n):
            dp_now = max(dp_i, dp_pre + nums[i])
            dp_pre = dp_i
            dp_i = dp_now
        return dp_i


class SolutionT213(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        return max(SolutionT198().rob3(nums[1:]), SolutionT198().rob3(nums[:-1]))

    def helper(self, nums):
        n = len(nums)
        dp_pre = 0
        dp_i = 0

        for i in range(n):
            dp_now = max(dp_i, dp_pre + nums[i])
            dp_pre = dp_i
            dp_i = dp_now
        return dp_i


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionT337(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 这里dfs其实也是树形DP模板
        def dfs(node):
            if not node:
                return [0, 0]   # [不包含当前结点、只包含左右子结点的累计最大值, 包含当前结点、加上左右子结点的子"不包含当前结点、只包含左右子结点的累计最大值"]

            l = dfs(node.left)
            r = dfs(node.right)

            return [max(l) + max(r), node.val + l[0] + r[0]]

        return max(dfs(root))


if __name__ == '__main__':
    test = [1, 2, 3, 1]
    test2 = [2, 7, 9, 3, 1]
    test3 = [2, 1, 1, 2]
    test4 = [1, 1]

    # test5 = [3, 2, 3, null, 3, null, 1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)


    # print(SolutionT198().rob(test))
    # print(SolutionT198().rob2(test))

    # print(SolutionT198().rob(test2))
    # print(SolutionT198().rob3(test3))
    # print(SolutionT198().rob2(test4))

    print(SolutionT337().rob(root))
