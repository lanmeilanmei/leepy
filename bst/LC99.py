"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""
# notes: 解法1 average O(lgn) space (worst case O(n) space)
#        解法2 average O(lgn) space (worst case, O(n) space)
from test.trees.trees import TreeNode
import sys


class SolutionT99(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        pre, stack, first, second = None, [], None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            if pre and pre.val > node.val:
                if first is None:
                    first = pre
                second = node
            pre = node
            root = node.right
        first.val, second.val = second.val, first.val # 结构不变, 只交换值

    def recoverTree_DFS(self, root):
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.pre.val > node.val:
                if not self.first:
                    self.first = self.pre   # 记录第一次出错处, 记录较大值,
                self.second = node          # 记录较小值, 如果当前结点不是最终swap出错处, 则会更新结束
            self.pre = node                 # 更新当前极小值结点, 目的是找到最终swap结点
            inorder(node.right)

        self.pre = TreeNode(-sys.maxsize-1)
        self.first, self.second = None, None
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def recoverTree_deprecated(self, root):
        def inorder(node):
            if not node: return None
            le = inorder(node.left)
            ri = inorder(node.right)
            if le and node.left.val > node.val: # 左结点大于当前结点
                left = node.left.left
                right = node.left.right
                node.left.left = node
                node.left.right = node.right
                node.left = left
                node.right = right
            if ri and node.right.val < node.val:
                left = node.right.left
                right = node.right.right
                node.right.right = node
                node.right.left = node.right
                node.left = left
                node.right = right
            return node

        return inorder(root)


if __name__ == '__main__':
    from test.bst.bst import BSTtrees
    SolutionT99().recoverTree(BSTtrees.bst_99())