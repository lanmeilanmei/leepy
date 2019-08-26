"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""
# notes: 第二种 Time complexity: O(n)  Space compleixty: O(n)


class SolutionT230(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node, res):
            if not node: return
            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)

        rs = []
        dfs(root, rs)
        return rs[k-1]

    def kthSmallest_2(self, root, k):
        def inorder(node):
            if not node: return -1
            x = inorder(node.left)     # 一直访问到最左端结点
            if self.k == 0: return x           # 如果找到指定值, 则需要在当前层将目标值返回给dfs上层调用
            self.k -= 1
            if self.k == 0: return node.val
            return inorder(node.right) # 未找到, 则进入node.right, 也是方便左右寻找完返回上层

        self.k = k
        return inorder(root)

    def kthSmallest_Iteratively(self, root, k):
        stack, node, ct = [], root, 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            ct += 1
            if ct == k: return node.val  # 题目有说明k始终有效
            node = node.right
        return -1   # 额外添加, 找不到返回-1
