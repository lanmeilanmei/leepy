import unittest


class SearchTest(unittest.TestCase):
    def test_lc17(self):
        from search.LC17 import SolutionT17
        self.assertEqual(SolutionT17().letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_lc39(self):
        from search.LC39 import SolutionT39
        self.assertEqual(SolutionT39().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(SolutionT39().combinationSum_order([2, 3, 6, 7], 7), [[7], [2, 2, 3]])
