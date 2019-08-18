"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# notes: similar to LC102
# 避免结尾反转列表, 可以在合适地方 list.insert(0. []), 详细代码参考如下链接
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue).


class SolutionT107(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, depth, res):
            if not node: return
            while len(res) <= depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1, res)
            dfs(node.right, depth + 1, res)

        ans = []
        dfs(root, 0, ans)
        return list(reversed(ans))

    def levelOrderBottomBFS(self, root):
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
        return list(reversed(res))
