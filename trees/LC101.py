"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

# require recursively + iteratively
# notes: recursively --> 77/32


class SolutionT101(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.__mirror(root.left, root.right)

    def __mirror(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        left = self.__mirror(p.left, q.right)
        right = self.__mirror(p.right, q.left)
        return p.val == q.val and left and right


