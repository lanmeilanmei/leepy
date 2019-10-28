"""
138. 复制带随机指针的链表
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深拷贝。 

输入：
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

解释：
节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
 

提示：

你必须返回给定头的拷贝作为对克隆列表的引用。
"""
# 解法1/2 dfs/ 栈
# 时间复杂度：O(N) 其中 N 是链表中节点的数目。
# 空间复杂度：O(N) 需要维护一个已访问字典。渐进时间复杂度为 O(N)


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(node):
            if node is None:
                return None

            if node in visitedHash:
                return visitedHash[node]

            copy_node = Node(node.val, None, None)
            visitedHash[node] = copy_node

            copy_node.next = dfs(node.next)
            copy_node.random = dfs(node.random)

            return copy_node

        visitedHash = {}
        return dfs(head)

    def copyRandomList_2(self, head):

        def getCloneNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
            return None

        if head is None:
            return head

        visited = {}
        old_node = head

        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        while old_node is not None:
            new_node.random = getCloneNode(old_node.random)
            new_node.next = getCloneNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

        return visited[head]
