"""
965. Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:
     1
    / \
   1   1
  / \   \
 1   1   1

Input: [1,1,1,1,1,null,1]
Output: true
Example 2:
     2
    / \
   2   2
  / \
 5   2

Input: [2,2,2,5,2]
Output: false

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""
# notes: 11/16  50/83 + return 94/66    50/91 [T:O(n), S:O(h)]
# 2th method is similar to LC100


class SolutionT965(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        val = root.val
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                if curr.val != val:
                    return False
                stack.append(curr.right)
                stack.append(curr.left)
        return True

    def isUnivalTree_recursively(self, root):
        self.__isUnival = True

        def dfs(node, val):
            if not node: return
            if node.val != val:
                self.__isUnival = False
                return
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, root.val)
        return self.__isUnival

    def isUnivalTree_recursively_hh(self, root):
        if not root: return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree_recursively_hh(root.left) and self.isUnivalTree_recursively_hh(root.right)
