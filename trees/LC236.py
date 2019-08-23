"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [-10, 9, 20, null, null, 15, 7]

       -10
       / \
      9  20
        /  \
       15   7
Example 1:

Input: root = [-10, 9, 20, null, null, 15, 7], p = 9, q = 7
Output: -10
Explanation: The LCA of nodes 9 and 7 is -10
Example 2:

Input: root = [-10, 9, 20, null, null, 15, 7], p = 20, q = 7
Output: 20
Explanation: The LCA of nodes 20 and 7 is 20, since a node can be a descendant of itself according to the LCA definition.
"""
# notes: by_hh Time complexity: O(n) Space complexity: O(h)
# 注意 dfs return 基础条件
# 后两种迭代暂未


# TODO iteratively method not understood
class SolutionT236(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if any((not root, root == p, root == q)): return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left or not right: # 至少有一个未找到
            return left if left else right
        return root

    def lowestCommonAncestor_2(self, root, p, q):
        res = []
        stack = [[root, res]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in [None, p, q]:
                parent += node
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                parent += node if all(subs) else max(subs),
        return res[0]

    def lowestCommonAncestor_3(self, root, p, q):
        def path(root, goal):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == goal:
                            return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()

        return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)
