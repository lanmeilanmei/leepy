"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# notes: search in dfs 40/71  dfs_iteratively 65/85


# TODO method by hh, not passed
class SolutionT113(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.__dfs(root, sum, [root.val], res)
        return res

    def __dfs(self, node, k, path, res):
        if not node.left and not node.right:
            if sum(path) == k:
                res.append(path[:])
            return

        if node.left:
            path.append(node.left.val)
            self.__dfs(node.left, k, path, res)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.__dfs(node.right, k, path, res)
            path.pop()

    # def pathSum_hh(self, root, sum):
    #     res = []
    #     self.__dfs_hh(root, sum, [], res)
    #     return res
    #
    # def __dfs_hh(self, node, k, path, res):
    #     if not node: return
    #     if not node.left and not node.right:
    #         if node.val == k:
    #             path.append(node.val)
    #             res.append(path[:])
    #         return
    #     path.append(node.val)
    #     new_k = k - node.val
    #     self.__dfs_hh(node.left, new_k, path, res)
    #     self.__dfs_hh(node.right, new_k, path, res)
    #     path.pop()

    def pathSum_iteratively(self, root, s):
        if not root: return []
        res, stack = [], [(root, [root.val], s)]
        while stack:
            curr, path, k = stack.pop()
            if not curr.left and not curr.right and curr.val == k:
                res.append(path[:])
            if curr.right:
                stack.append((curr.right, path+[curr.right.val], k-curr.val))
            if curr.left:
                stack.append((curr.left, path+[curr.left.val], k-curr.val))
        return res
