"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
import sys
# notes: similar to LC124 but easy
# Time complexity O(n), Space complexity O(h)
# Time complexity O(n), Space complexity O(n)


# TODO complexity analysis
class SolutionT543(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.__helper(root)
        return self.ans

    def __helper(self, root):
        if not root: return -1  # 若这里为0,则返回时需要+1, 然后left/right无需+1, 这里与下面方法参数保持一致性
        left = self.__helper(root.left) + 1
        right = self.__helper(root.right) + 1
        self.ans = max(self.ans, left + right)
        return max(left, right)

    def diameterOfBinaryTreeIteratively(self, root):
        """
        很巧妙的一个方法
        前序遍历添加结点进栈, 路径长度计算由初始字典{None: 0}配合出栈结点自底向上累加可得
        路径长度的维护原则和某结点的最大路径, 都和上面dfs一致
        """
        if not root: return 0
        nodeDict = {None: -1}
        res, stack = 0, [root]
        while stack:
            node = stack[-1]
            if node.left in nodeDict and node.right in nodeDict:
                stack.pop()
                left = nodeDict[node.left] + 1
                right = nodeDict[node.right] + 1
                res = max(res, left + right)
                nodeDict[node] = max(left, right)
            else:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return res

