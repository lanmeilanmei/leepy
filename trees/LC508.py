"""
508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
# notes:


class SolutionT508(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.res[s] += 1
            return s

        if not root: return []
        self.res = Counter()
        dfs(root)
        maxct = max(self.res.values())
        return [k for k in self.res.keys() if self.res[k] == maxct]

    def __helper_deprecated(self, node, res):
        if not node: return 0
        res.append(node.val)
        if node.left or node.right:
            left = self.__helper(node.left, res)
            right = self.__helper(node.right, res)
            res.append(left + right + node.val)
        else:
            return node.val
        # if not node.left and not node.right:
        #     res.append(node.val)
        # res.extend([node.val, left + right + node.val])
