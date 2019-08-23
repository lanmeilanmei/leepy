"""
235. Lowest Common Ancestor of a Binary Search Tree

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

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""
# notes: similar to lc236


class SolutionT235(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in [None, p, q]: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left or not right:
            return left if left else right
        return root

    def lowestCommonAncestor_2(self, root, p, q):
        if not root: return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

    def lowestCommonAncestor_3(self, root, p, q):
        node = root
        while node:
            if q.val < node.val > p.val:
                node = node.left
            elif q.val > node.val < p.val:
                node = node.right
            else:
                return node
