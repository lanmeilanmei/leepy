"""
530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""
# notes: similar to LC98
# 解法1 O(n) space  解法2 O(h) space


class SolutionT530(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node, res): # 中序遍历得到list, 两两比较
            if not node: return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

        rs = []
        inorder(root, rs)
        diff = rs[-1]
        for i in range(1, len(rs)):
            diff = min(diff, rs[i]-rs[i-1])
        return diff

    def getMinimumDifference_2(self, root):
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.pre:
                self.mindiff = min(self.mindiff, node.val-self.pre.val)
            self.pre = node
            inorder(node.right)

        self.pre = None
        self.mindiff = float("inf")
        inorder(root)
        return self.mindiff

    def getMinimumDifference_Iteratively(self, root): # 解法2的迭代中序实现, similar to LC98
        stack, node = [], root
        mindiff = float("inf")
        pre = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if pre:
                mindiff = min(mindiff, node.val - pre.val)
            pre = node
            node = node.right
        return mindiff
