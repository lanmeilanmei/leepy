"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# notes: 两种方法都是 Time complexity: O(n) Space complexity: O(n)
#        第二、三种思路一致, 但第三种略快


class SolutionT98(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, vmin, vmax): # 每一次dfs都有上下界限定进行判断
            if not node: return True
            if (vmin is not None and node.val <= vmin) or (vmax is not None and node.val >= vmax): # 避免vmin/vmax为0导致真值误判
                return False
            return dfs(node.left, vmin, node.val) and dfs(node.right, node.val, vmax)

        return dfs(root, None, None)

    def isValidBST_2(self, root):
        def inorder(node):  # 先访问当前树的最左结点, 获得极小值, 每次只需判断当前结点和pre即可
            if not node: return True
            if not inorder(node.left): return False
            if self.pre is not None and node.val <= self.pre.val: return False
            self.pre = node
            return inorder(node.right)

        self.pre = None
        return inorder(root)

    def isValidBST_Iteratively(self, root):
        """
        基于isValidBST_2的思想, 这里用迭代式中序遍历实现
        具体见test.trees.trees.template_inorder_iteratively
        """
        stack, node = [], root
        pre = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if pre and node.val <= pre.val: return False
            pre = node
            node = node.right
        return True

    # 只考虑到浅层左右大小关系, 未考虑到全局的左右结点都与根结点大小有关
    def isValidBST_deprecated(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node: return
            if (node.left and node.left.val >= node.val) or (node.right and node.right.val <= node.val):
                self.res = False
            dfs(node.left)
            dfs(node.right)

        self.res = True
        dfs(root)
        return self.res
