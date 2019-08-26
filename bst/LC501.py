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


# TODO not finish yet
class SolutionT501(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def visit(val):
            if self.ct > 0 and self.val == val:
                self.ct += 1
            else:
                self.val = val
                self.ct = 1

            if self.ct > self.maeks:
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
