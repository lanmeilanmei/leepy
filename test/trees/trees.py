class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_binary_tree():
    """
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def get_binary_tree_02():
    """
    Given binary tree [3,9,20,null,null,15,7,9],
        1
       / \
      9  20
        /  \
       15   7
            \
             9
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(9)
    return root


def get_binary_tree_03():
    """
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    return root


def get_symmetric_tree():
    """
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    return root


def get_flip_equivalent_tree_a():
    """
         1
       /  \
      2    3
     / \   /
    4  5  6
      / \
     7   8
    """
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)

    return root


def get_flip_equivalent_tree_b():
    """
          1
       /   \
      3     2
       \   / \
       6  4   5
             / \
            8   7
    """
    root = TreeNode(1)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(7)

    root.left = TreeNode(3)
    root.left.right = TreeNode(6)

    return root
