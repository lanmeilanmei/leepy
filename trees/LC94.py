"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# notes: 73/6  41/82  41/50


class SolutionT94(object):
    def inorderTraversal(self, root):
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

    def inorderTraversal_loop(self, root):
        if not root: return []
        res = []
        stack = [(root, 0)]
        while stack:
            curr, is_visited = stack.pop()
            if curr:
                if is_visited:
                    res.append(curr.val)
                else:
                    stack.append((curr.right, 0))
                    stack.append((curr, 1))
                    stack.append((curr.left, 0))
        return res

    def inorderTraversal_recursively(self, root):
        def dfs(node, res):
            if not node: return
            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)

        res = []
        dfs(root, res)
        return res

