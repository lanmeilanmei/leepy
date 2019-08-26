# leepy/trees/notes 第5条 create a bst
from test.trees.trees import TreeNode


class BSTtrees(object):
    def createBST(self, nums):
        root = None
        for num in nums:
            root = self.insert(root, num)
        return root

    def insert(self, root, val):
        if not root: return TreeNode(val)
        if val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def inorder(self, root):
        def dfs(node, rs):
            if not node: return
            dfs(node.left, rs)
            rs.append(node.val)
            dfs(node.right, rs)

        res = []
        dfs(root, res)
        return res

    @classmethod
    def bst_1(cls, negtive=True):
        """
                2
               / \
              1   3
        """
        if negtive:
            root = TreeNode(2)
            root.left = TreeNode(1)
            root.right = TreeNode(3)
        else:
            root = TreeNode(1)
            root.left = TreeNode(1)
        return root

    @classmethod
    def bst_2(cls):
        root = TreeNode(0)
        root.right = TreeNode(-1)
        return root
