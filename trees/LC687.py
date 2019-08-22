"""
687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# notes: similar to LC543 + LC124


class SolutionT687(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.__helper(root)
        return self.res

    def __helper(self, root):
        """
        先将dfs的地基条件考虑清楚: 叶子结点 or 单边且值不同的结点 or 双边且值不同的结点, 此时路径长度都应该为0
        由于地基条件中root.val == root.child.val已经先行过滤(同则增大, 异则置0), self.res 仍可以取单边路径较大者
       """
        left = self.__helper(root.left) if root.left else -1
        right = self.__helper(root.right) if root.right else -1
        pathLeft = left + 1 if left >= 0 and root.val == root.left.val else 0
        pathRight = right + 1 if right >= 0 and root.val == root.right.val else 0
        self.res = max(self.res, pathLeft + pathRight)
        return max(pathLeft, pathRight)
