"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""
# notes:
# 1st, by self, 因为path的创建及取出,耗时略多
# dfs recursively
# dfs + stack


class SolutionT129(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = []
        self.__helper(root, [], res)
        s = 0
        for nums in res:
            i = 0
            for num in nums:
                s += num * pow(10, i)
                i += 1
        return s

    def __helper(self, root, path, res):
        if not root: return
        if not root.left and not root.right:
            path.insert(0, root.val)
            res.append(path[:])
            return
        self.__helper(root.left, [root.val] + path, res)
        self.__helper(root.right, [root.val] + path, res)

    # recursively
    def sumNumbers_2(self, root):
        def dfs(node, value):
            if not node: return
            if not node.left and not node.right:
                self.ct += value*10 + node.val
            dfs(node.left, value*10 + node.val)
            dfs(node.right, value*10 + node.val)

        self.ct = 0
        dfs(root, 0)
        return self.ct

    # dfs + stack 用双端队列则需要修改出队deque.popleft
    # 自顶向下累加, (v1 * 10 + v2) * 10 + v3
    def sumNumbers_3(self, root):
        if not root: return 0
        res, stack = 0, [(root, root.val)]
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10 + node.right.val))
                if node.left:
                    stack.append((node.left, value*10 + node.left.val))
        return res
