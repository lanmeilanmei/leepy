"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

判断叶子结点是否相同

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""
# notes: 88/75  98/62  88/12
# 关键在于叶子结点的添加顺序是中序遍历的结果 [详细中序遍历的三种方式]


class SolutionT872(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.inorder_leaf(root1) == self.inorder_leaf(root2)

    def inorder_leaf(self, root):
        if not root: return []
        res, stack = [], []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if not curr.left and not curr.right:
                res.append(curr.val)
            curr = curr.right
        return res

    def leafSimilarDFS(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.inorder_dfs_leaf(root1) == self.inorder_dfs_leaf(root2)

    def inorder_dfs_leaf(self, root):
        def dfs(node, res):
            if not node: return
            dfs(node.left, res)
            if not node.left and not node.right:
                res.append(node.val)
            dfs(node.right, res)

        ans = []
        dfs(root, ans)
        return ans

    def leafSimilarByLoop(self, root1, root2):
        return self.inorder_loop_leaf(root1) == self.inorder_loop_leaf(root2)

    def inorder_loop_leaf(self, root):
        if not root: return
        res, stack = [], [(root, 0)]
        while stack:
            curr, is_visited = stack.pop()
            if curr:
                if is_visited:
                    if not curr.left and not curr.right:
                        res.append(curr.val)
                else:
                    stack.append((curr.right, 0))
                    stack.append((curr, 1))
                    stack.append((curr.left, 0))
        return res

