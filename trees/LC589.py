"""
589. N-ary Tree Preorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

         1
       / \ \
      3  2  4
    /  \
   5   6

Return its preorder traversal as: [1,3,5,6,2,4].

Note:

Recursive solution is trivial, could you do it iteratively?
"""
# notes: 93/88    9/8   65/80


# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class SolutionT589(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children[::-1])
        return res

    def preorder_recursively(self, root):
        def dfs(curr, re):
            if not curr: return
            re.append(curr.val)
            for node in curr.children:
                dfs(node, re)

        res = []
        dfs(root, res)
        return res

    def preorder_loop(self, root):
        if not root: return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, is_visited = stack.pop()
            if node:
                if is_visited:
                    res.append(node.val)
                else:
                    for child in node.children[::-1]:
                        stack.append((child, 0))
                    stack.append((node, 1))
        return res

