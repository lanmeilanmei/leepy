"""
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# notes:


class SolutionT257(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path, res):
            if not node: return
            if not node.left and not node.right:
                path += "->{0}".format(node.val)
                res.append(path[2:])

            dfs(node.left, path + "->{0}".format(node.val), res)
            dfs(node.right, path + "->{0}".format(node.val), res)

        if not root: return []
        ans = []
        dfs(root, "", ans)
        return ans

    # dfs + stack
    def binaryTreePaths_2(self, root):
        if not root: return []
        res, stack = [], [(root, "")]
        while stack:
            node, currStr = stack.pop()
            if not node.left and not node.right:
                res.append(currStr + str(node.val))
            if node.right:
                stack.append((node.right, currStr + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, currStr + str(node.val) + "->"))
        return res

    # same as the first but conciser
    def binaryTreePaths_3(self, root):
        def dfs(node, path, res):
            if not node: return
            if not node.left and not node.right:
                path += str(node.val)
                res.append(path)

            dfs(node.left, path + str(node.val) + "->", res)
            dfs(node.right, path + str(node.val) + "->", res)

        if not root: return []
        ans = []
        dfs(root, "", ans)
        return ans
