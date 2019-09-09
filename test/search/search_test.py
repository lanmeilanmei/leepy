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
