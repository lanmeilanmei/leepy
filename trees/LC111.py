"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# notes: 常用递归用法, 22/38


class SolutionT111(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left:
            return 1 + right
        if not root.right:
            return 1 + left
        return min(left, right) + 1

