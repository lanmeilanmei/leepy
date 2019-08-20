"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# notes: dfs --> Time complexity: O(n^2) Space complexity: O(n)
#       pathSumBetter --> Time complexity: O(n) Space complexity: O(h)


# TODO unfinished: A method with specific paths returned
class SolutionT437(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(node, left):
            if not node: return 0
            left -= node.val
            return (1 if left == 0 else 0) + dfs(node.left, left) + dfs(node.right, left)

        if not root: return 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSum_1(self, root, sum):
        def find_paths(root, target):
            if root:
                return int(root.val == target) + find_paths(root.left, target-root.val) + find_paths(root.right, target-root.val)
            return 0

        if root:
            return find_paths(root, sum) + self.pathSum_1(root.left, sum) + self.pathSum_1(root.right, sum)
        return 0

    def pathSumBetter(self, root, sum):
        self.result = 0
        self.__helper(root, sum, 0, {0: 1})     # 考虑到单结点自身符合条件, cache初始化{0: 1}
        return self.result

    def __helper(self, root, target, so_far, cache):
        if not root: return
        complement = so_far + root.val - target # 判断当前累计和与target差值
        if complement in cache:                 # 若差值已被记录, 则以当前结点为终点的所在路径符合要求
            self.result += cache[complement]
        cache.setdefault(so_far+root.val, 0)    # 负责记录当前累计和, 无论是否符合要求都初始化为1, 表示访问过1次
        cache[so_far+root.val] += 1             # 因为符合要求的次数已被记录在result中
        self.__helper(root.left, target, so_far+root.val, cache)
        self.__helper(root.right, target, so_far + root.val, cache)
        cache[so_far+root.val] -= 1             # 结束以当前结点开始的路径查找
