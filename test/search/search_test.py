import unittest


class SearchTest(unittest.TestCase):
    def test_lc17(self):
        from search.LC17 import SolutionT17
        self.assertEqual(SolutionT17().letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_lc39(self):
        from search.LC39 import SolutionT39
        self.assertEqual(SolutionT39().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(SolutionT39().combinationSum_order([2, 3, 6, 7], 7), [[7], [2, 2, 3]])

    def test_lc40(self):
        from search.LC40 import SolutionT40
        self.assertEqual(SolutionT40().combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])

    def test_lc216(self):
        from search.LC216 import SolutionT216
        self.assertEqual(SolutionT216().combinationSum3(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]])

    def test_lc377(self):
        from search.LC377 import SolutionT377
        self.assertEqual(SolutionT377().combinationSum4([1, 2, 3], 4), 7)
        self.assertEqual(SolutionT377().combinationSum4([1, 2, 3], 3), 4)

    def test_lc77(self):
        from search.LC77 import SolutionT77
        self.assertEqual(SolutionT77().combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

    def test_lc78(self):
        from search.LC78 import SolutionT78
        self.assertEqual(SolutionT78().subsets([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        self.assertEqual(SolutionT78().subsets_BFS([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def test_lc90(self):
        from search.LC90 import SolutionT90
        self.assertEqual(SolutionT90().subsetsWithDup([1, 2, 2]), [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])

    def test_lc47(self):
        from search.LC47 import Solution
        self.assertEqual(Solution().permuteUnique([1, 1, 2]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    def test_lc784(self):
        from search.LC784 import Solution
        self.assertEqual(Solution().letterCasePermutation("a1b2"), ["a1b2", "a1B2", "A1b2", "A1B2"])
