"""
814. Binary Tree Pruning

题目大意：把不含有1的节点的子树全部删除
         1
        / \
       0   1
      / \
     0   1

         1
        / \
       0   1
        \
         1
"""
# notes:    48/66 [O(n),O(h)]


class SolutionT814(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 1 or root.left or root.right:
            return root
        else:  # root.val != 1 and root.left is None and root.right is None
            return None
