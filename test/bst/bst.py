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
    def bst_2(cls, negtive=True):
        if negtive:
            root = TreeNode(0)
            root.right = TreeNode(-1)
        else:
            root = TreeNode(1)
            root.right = TreeNode(3)
            root.right.left = TreeNode(2)
        return root

    @classmethod
    def bst_230(cls):
        """
           3
          / \
         1   4
          \
           2
        """
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        return root

    @classmethod
    def bst_99(cls, correct=False):
        """
           1
          /
         3
          \
           2
        """
        if correct:
            root = TreeNode(3)
            root.left = TreeNode(1)
            root.left.right = TreeNode(2)
        else:
            root = TreeNode(1)
            root.left = TreeNode(3)
            root.left.right = TreeNode(2)
        return root

    @classmethod
    def bst_501(cls, extend=False):
        """ 4、3 都可切成 5
           4
         /  \
        2    6
       / \  / \
      1  3  5  6
        """
        if not extend:
            root = TreeNode(1)
            root.right = TreeNode(2)
            root.right.left = TreeNode(2)
            return root
        else:
            root = TreeNode(5)
            root.left, root.right = TreeNode(2), TreeNode(6)
            root.left.left, root.left.right = TreeNode(1), TreeNode(3)
            root.right.left, root.right.right = TreeNode(5), TreeNode(6)
            return root
