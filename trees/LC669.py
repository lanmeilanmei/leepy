"""
669. Trim a Binary Search Tree

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""
# notes:    43/44 [O(n), O(1)]
# 二叉搜索树中删除一个结点 的变形, 实现"删除"操作需要合适的结点来替换
# 如果当前结点curr, 有 curr.val 不在[L, R]区间内, 根据 BST 性质,
# 尝试寻找其右子结点替换(当curr.val < L) 或 寻找其左子结点替换(当curr.val > R)


# classic
class SolutionT669(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root: return root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

