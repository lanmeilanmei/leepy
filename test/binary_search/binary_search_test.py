import unittest
from test.binary_search.binary_search_data import BinarySearchData


class BinarySearchTest(unittest.TestCase):
    def test_examples(self):
        from binary_search.Examples import SolutionEx
        self.assertEqual(SolutionEx().binary_search_01(BinarySearchData.A, 8, 0, 6), 4)
        # self.assertEqual(SolutionEx().binary_search_01(BinarySearchData.A, 6, 0, 6), -1)
