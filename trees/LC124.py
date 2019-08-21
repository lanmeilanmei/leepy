"""
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# notes: by_hh --> Time complexity O(n), Space complexity O(h)
# 返回树中路径最大的和, 路径可以无需经过root, 但是相邻可连通的
# 相当于当作无向图中找到两顶点之间的路径最大值,不能同时返回左右结点, 除非是倒数第二层的结点
# related LC687 + LC543
import sys


class SolutionT124(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = -sys.maxsize
        self.__helper(root)
        return self.ans

    def __helper(self, root):
        if not root: return -sys.maxsize
        left = max(0, self.__helper(root.left))
        right = max(0, self.__helper(root.right))           # 后序遍历, 方便最后比较单边最大连通值和加上根结点后的双边连通值
        self.ans = max(self.ans, root.val + left + right)   # 基于left/right保证连通性基础上, 记录加上当前根结点值, 相当于以当前根结点为子树的单边连通总和
        return root.val + max(left, right)                  # 返回单边总和最大值, 保证连通性!!! 这里每次返回给left or right 的值保证了连通性
                                                            # 这里返回给上层后, 供上层根结点更新self.ans, 并选择其left/right的较大者
    # self.ans 记录了局部连通性的最大总和
