"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
         1
       / \ \
      3  2  4
    /  \
   5   6

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""
# notes: bfs  dfs  similar to lc102 and lc107


class SolutionT429(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        res= []
        curr, down = [root], []
        while curr:
            tmp = []
            for node in curr:
                tmp.append(node.val)
                down.extend(node.children)
            res.append(tmp)
            curr = down
            down = []
        return res

    def levelOrder_DFS(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        def dfs(node, depth, res):
            if node:
                while len(res) <= depth:
                    res.append([])
                res[depth].append(node.val)
                for child in node.children:
                    dfs(child, depth+1, res)

        ans = []
        dfs(root, 0, ans)
        return ans
