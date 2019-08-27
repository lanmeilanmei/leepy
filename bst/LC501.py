"""
501. Find Mode in Binary Search Tree 找到BST中出现次数最多的元素

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
"""
# notes: 这题注意配合bst_501输入理解，注意到BST特性, 如果有重复值，则中序遍历时该重复值到X轴上的坐标一定是相邻的
# 弄清这一点后，剩下的就是理解 visit 方法的处理逻辑了
# 解法1 Time complexity: O(n) Space complexity: O(n)
# 解法2 Time complexity: O(n) Space complexity: O(1) Two passes. First pass to find the count of the mode, second pass to collect all the modes.


# TODO review
class SolutionT501(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def visit(val):
            if self.ct > 0 and self.val == val:     # 遇到重复值时, ct累加
                self.ct += 1
            else:
                self.val = val                      # 这里self.ct=0, 初始化参数
                self.ct = 1

            if self.ct > self.maeks:    # 一旦有新的最高频词出现, 初始化self.ans, 只装载该高频词
                self.maeks = self.ct
                self.ans = []

            if self.ct == self.maeks:
                self.ans.append(val)

        def inorder(node):
            if not node: return
            inorder(node.left)
            visit(node.val)
            inorder(node.right)

        self.ct, self.val, self.maeks = 0, 0, 0
        self.ans = []
        inorder(root)
        return self.ans

    def findMode_2(self, root):
        import sys
        def visit(val):
            if self.ct > 0 and self.val == val:
                self.ct += 1
            else:
                self.val = val
                self.ct = 1

            if self.ct > self.maeks:
                self.maeks = self.ct

            if self.ct == self.modect:
                self.ans.append(val)

        def inorder(node):
            if not node: return
            inorder(node.left)
            visit(node.val)
            inorder(node.right)

        """ 
        第一遍求maeks, 第二遍找符合maeks的值
        """
        self.ct, self.val, self.maeks = 0, 0, 0
        self.modect = sys.maxsize
        self.ans = []
        inorder(root)
        self.modect = self.maeks
        self.ct = 0
        inorder(root)
        return self.ans
