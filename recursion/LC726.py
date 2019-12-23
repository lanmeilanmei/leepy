"""
726. 解析化学表达式

从右向左检查每个字符
如果字符为数字，将其添加到当前计数器
如果字符是')'，乘以系数并将计数器添加到栈
如果字符是')'，不用将下一个元素与最后的计数器相乘，删除最后的计数器并将其除以最后一个计数器
如果字符为大写字母，需要将元素及其系数添加到字典
如果字符为小写字母，仅将字符添加到当前元素即可
将字典中的键值对排序并返回
"""
import collections


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0

        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ")":
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == "(":
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ""
                i = cnt = 0
            elif c.islower():
                elem += c
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))


if __name__ == '__main__':
    # print(Solution().countOfAtoms("Mg(OH)2"))
    print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
