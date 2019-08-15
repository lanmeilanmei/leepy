"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# notes: O(n) 99/6   O(nlgn) 6/100


# TODO complexity analysis
class SolutionT110(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.__balanced = True

        def height(root):
            if not root or not self.__balanced: return 0
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1:
                self.__balanced = False
                return 0
            return max(left, right) + 1

        height(root)
        return self.__balanced

    def isBalanced_(self, root):
        if not root: return True
        left = self.__height(root.left)
        right = self.__height(root.right)
        return (abs(left - right) <= 1) and self.isBalanced_(root.left) and self.isBalanced_(root.right)

    def __height(self, root):
        if not root: return 0
        return max(self.__height(root.left), self.__height(root.right)) + 1
