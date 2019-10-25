"""
克隆图
"""
# 图的 dfs、bfs 遍历


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def dfs(curr_node):
            if not curr_node:
                return

            if curr_node in dic:
                return dic[curr_node]

            clone = Node(curr_node.val, [])
            dic[curr_node] = clone

            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        dic = {}
        return dfs(node)

    def cloneGraph_BFS(self, node):
        from collections import deque
        dic = {}

        if not node:
            return
        clone = Node(node.val, [])
        dic[node] = clone

        queue = deque()
        queue.appendleft(node)
        while queue:
            tmp = queue.pop()
            for neighbor in tmp.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(neighbor.val, [])
                    queue.appendleft(neighbor)
                dic[tmp].neighbors.append(dic[neighbor])

        return clone



