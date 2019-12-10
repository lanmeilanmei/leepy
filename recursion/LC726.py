"""

"""
import collections


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def parse():
            N = len(formula)
            count = collections.Counter()
            while self.i < N and formula[self.i] != ")":
                if formula[self.i] == "(":
                    self.i += 1
                    for name, v in parse().items():
                        pass

        self.i = 0
        ans = []
        dic = parse()
        for name in sorted(dic):
            ans.append(name)
            num = dic[name]
            if num > 1:
                ans.append(str(num))
        return "".join(ans)

