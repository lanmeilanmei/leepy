import unittest
from test.binary_search.binary_search_data import BinarySearchData


class BinarySearchTest(unittest.TestCase):
    def test_examples(self):
        from binary_search.Examples import SolutionEx
        self.assertEqual(SolutionEx().binary_search_01(BinarySearchData.A1, 8, 0, 6), 4)
        self.assertEqual(SolutionEx().binary_search_01(BinarySearchData.A1, 6, 0, 6), -1)

        self.assertEqual(SolutionEx().lower_bound(BinarySearchData.A2, 2, 0, 7), 1)
        self.assertEqual(SolutionEx().lower_bound(BinarySearchData.A2, 3, 0, 7), 4)
        self.assertEqual(SolutionEx().lower_bound(BinarySearchData.A3, 3, 0, 5), 2)

        self.assertEqual(SolutionEx().upper_bound(BinarySearchData.A2, 5, 0, 7), 7)
        self.assertEqual(SolutionEx().upper_bound(BinarySearchData.A2, 2, 0, 7), 4)

    def test_lc35(self):
        from binary_search.LC35 import SolutionT35
        self.assertEqual(SolutionT35().searchInsert(BinarySearchData.A35, 5), 2)
        self.assertEqual(SolutionT35().searchInsert(BinarySearchData.A35, 7), 4)
        self.assertEqual(SolutionT35().searchInsert(BinarySearchData.A35, 0), 0)

