"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# notes: bfs 99/93  dfs 13/10
# bfs 当前层的结点进栈1, 遍历当前层结点值添加到结果容器中, 同时将下一层(子结点)的结点进栈2
# dfs 方法支持前中后序三种方式, dfs先根据不同深度预生成列表


class SolutionT102(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        curr, down = [root], []
        while curr:
            tmp = []
            for node in curr:
                tmp.append(node.val)
                if node.left:
                    down.append(node.left)
                if node.right:
                    down.append(node.right)
            res.append(tmp)
            curr = down
            down = []
        return res

    def levelOrderRecursively(self, root):
        def dfs(node, depth, res):
            if not node: return
            while len(res) <= depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1, res)
            dfs(node.right, depth+1, res)

        ans = []
        dfs(root, 0, ans)
        return ans
