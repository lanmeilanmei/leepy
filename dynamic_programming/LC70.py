"""
70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 最优解公式: f(x) = f(x-1) + f(x-2)
# 解法1： Time Complexity O(n), Space Complexity O(n)
# 解法2： Time Complexity O(n), Space Complexity O(1)


class Solutiont70(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

    def climbStairs_2(self, n):
        one, two, curr = 1
        for i in range(2, n+1):
            curr = one + two
            two = one
            one = curr
        return curr
