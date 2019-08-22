class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def definition_binary_search_tree(root, x):
    """
    Time Complexity: O(h)
    Worst case: O(h) = O(n), like single linked list
    Best case: O(h) = O(lgn), a balanced binary tree
    for a BST, the vals are sorted !!!
    """
    if not root:
        return False
    if x == root.val:
        return True
    if x < root.val:
        return definition_binary_search_tree(root.left, x)
    else:
        return definition_binary_search_tree(root.right, x)


# ----------递归遍历树, 关键在于每棵子树 root 的处理顺序----------

def template_preorder_recursively(root):
    if not root: return
    print(root.val)
    template_preorder_recursively(root.left)
    template_preorder_recursively(root.right)


def template_inorder_recursively(root):
    if not root: return
    template_preorder_recursively(root.left)
    print(root.val)
    template_preorder_recursively(root.right)


def template_postorder_recursively(root):
    if not root: return
    template_preorder_recursively(root.left)
    template_preorder_recursively(root.right)
    print(root.val)


# ----------循环遍历树, 关键在于 标记位is_visited 前后的数据进出顺序----------

def template_preorder_by_loop(root):
    res = []
    stack = [(root, 0)]
    while stack:
        node, is_visited = stack.pop()
        if node:
            if is_visited:
                res.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node.left, 0))
                stack.append((node, 1))
    return res


def template_inorder_by_loop(root):
    res = []
    stack = [(root, 0)]
    while stack:
        node, is_visited = stack.pop()
        if node:
            if is_visited:
                res.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))
    return res


def template_postorder_by_loop(root):
    res = []
    stack = [(root, 0)]
    while stack:
        node, is_visited = stack.pop()
        if node:
            if is_visited:
                res.append(node.val)
            else:
                stack.append((node, 1))
                stack.append((node.right, 0))
                stack.append((node.left, 0))
    return res


# ----------迭代遍历树, 关键在于结果添加的顺序 + 后序遍历双栈顺序----------

def template_preorder_iteratively(root):
    if not root: return []
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            res.append(curr.val)
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        curr = curr.right
    return res


def template_inorder_iteratively(root):
    if not root: return []
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


# 这里显式给出 stack_path, 强调结点在两栈进出的顺序
def template_postorder_iteratively(root):
    if not root: return []
    res, stack_node, stack_path = [], [], []
    curr = root
    stack_node.append(curr)
    while stack_node:
        curr = stack_node.pop()
        if curr.left:
            stack_node.append(curr.left)
        if curr.right:
            stack_node.append(curr.right)
        stack_path.append(curr.val)
    res.extend(reversed(stack_path))
    return res


# ----------迭代遍历树, 关键在于前序进栈的顺序, 以及逆后序----------

def template_preorder_iterative_hf(root):
    if not root: return []
    res, stack = [], []
    curr = root
    stack.append(curr)
    while stack:
        curr = stack.pop()
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
    return res


def template_postorder_iterative_hf(root):
    if not root: return []
    res, stack = [], []
    curr = root
    stack.append(curr)
    while stack:
        curr = stack.pop()
        if curr:
            res.append(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)
    return res[::-1]


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
        3
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


from trees.LC589 import Node


def get_multi_children_tree():
    """
         1
       / \ \
      3  2  4
    /  \
   5   6
    """
    c1 = Node(3, [Node(5), Node(6)])
    root = Node(1, [c1, Node(2), Node(4)])
    return root


def get_subtree_a(negtive=False):
    """
         3
        / \
       4   5
      / \
     1   2
    """
    root = TreeNode(3)

    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    if negtive:
        root.left.right.left = TreeNode(0)

    root.right = TreeNode(5)

    return root


def get_subtree_b():
    """
       4
      / \
     1   2
    """
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    return root


def get_unival_tree(negtive=False):
    """
         2
        / \
       2   2
      / \
     5   2
    """
    root = TreeNode(2)

    root.left = TreeNode(2)
    root.left.right = TreeNode(2)
    if negtive:
        root.left.left = TreeNode(5)

    root.right = TreeNode(2)

    return root


def get_pruned_tree(pruned=False):
    """
         1
        / \
       0   1
      / \
     0   1
    """
    root = TreeNode(1)

    root.left = TreeNode(0)
    root.left.right = TreeNode(1)
    if pruned:
        root.left.left = TreeNode(0)

    root.right = TreeNode(1)
    return root


def get_vertical_order_tree():
    """
         0
        / \
       8   1
         /   \
        3     2
        \     /
         4    5
         \   /
         7  6
    """
    root = TreeNode(0)
    root.left = TreeNode(8)
    root.right = TreeNode(1)

    root.right.left = TreeNode(3)
    root.right.left.right = TreeNode(4)
    root.right.left.right.right = TreeNode(7)

    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.left.left = TreeNode(6)

    return root


def get_pathSum_tree():
    """
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    """
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    return root


def get_maxSum_tree():
    """
       -10
       / \
      9  20
        /  \
       15   7
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def get_univalue_tree():
    """
              5
             / \
            4   5
           / \   \
          1   1   5
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)
    return root
