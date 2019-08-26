"""
700. Search in a Binary Search Tree
BST查找
"""
# 树的遍历方式, 见trees模块


class SolutionT700(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root
