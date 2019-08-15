"""
590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

          1
       / \ \
      3  2  4
    /  \
   5   6

Return its postorder traversal as: [5,6,3,2,4,1].
"""
# notes:    89/64   27/6    31/6


class SolutionT590(object):
    def postorder(self, root):
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
            stack.extend(curr.children)
        return res[::-1]

    def postorder_recursively(self, root):
        def dfs(node, re):
            if not node: return
            for child in node.children:
                dfs(child, re)
            re.append(node.val)

        res = []
        dfs(root, res)
        return res

    def postorder_loop(self, root):
        if not root: return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, is_visited = stack.pop()
            if node:
                if is_visited:
                    res.append(node.val)
                else:
                    stack.append((node, 1))
                    for child in node.children[::-1]:
                        stack.append((child, 0))
        return res
