"""
987. Vertical Order Traversal of a Binary Tree
树的垂直投影遍历, 同一位置按高度+值升序. 参数见下方函数注释
"""
# 第一种self, 线上测试未通过, 原因: 题意理解偏差. 返回是按数值有序, 实际是同一位置高度有序
# 第二种是记录了所有结点的位置, 再根据位置+值排序


class SolutionT987(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        left, right = 0, 0
        bound = [left, right]
        index = {0: []}
        self.dfs(root, 0, 0, bound, index, res)
        for i in range(bound[0], bound[1]+1):
            # ls = sorted(index[i])
            ls = index[i]
            res.append(ls)
        return res

    def dfs(self, node, x, y, bound, index, res):
        if not node: return
        if x < bound[0]:
            bound[0] -= 1
            index[x] = [node.val]
        elif x > bound[1]:
            bound[1] += 1
            index[x] = [node.val]
        else:
            index[x].append(node.val)
        self.dfs(node.left, x-1, y-1, bound, index, res)
        self.dfs(node.right, x+1, y-1, bound, index, res)

    def verticalTraversal_hh(self, root):
        def preorder(node, x, y, res):
            if not node: return
            res.append((x, y, node.val))
            preorder(node.left, x-1, y+1, res)
            preorder(node.right, x+1, y+1, res)

        if not root: return []
        ans, vals = [], []
        preorder(root, 0, 0, vals)
        last_x = -1000
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)
        return ans
