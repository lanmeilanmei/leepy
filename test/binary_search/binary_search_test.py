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

    def test_lc33(self):
        from binary_search.LC33 import SolutionT33
        self.assertEqual(SolutionT33().search_3([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(SolutionT33().search_4([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_lc81(self):
        from binary_search.LC81 import SolutionT81
        self.assertEqual(SolutionT81().search_2([2, 5, 6, 0, 0, 1, 2], 0), True)
        self.assertEqual(SolutionT81().search_2([2, 5, 6, 0, 0, 1, 2], 3), False)

    def test_lc153(self):
        from binary_search.LC153 import Solutiont153
        self.assertEqual(Solutiont153().findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(Solutiont153().findMin_2([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(Solutiont153().findMin_2([3, 4, 5, 1, 2]), 1)
        self.assertEqual(Solutiont153().findMin_2([2, 1]), 1)

        self.assertEqual(Solutiont153().findMin_3([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(Solutiont153().findMin_3([3, 4, 5, 1, 2]), 1)
        self.assertEqual(Solutiont153().findMin_3([2, 1]), 1)

        self.assertEqual(Solutiont153().findMin_4([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(Solutiont153().findMin_4([3, 4, 5, 1, 2]), 1)
        self.assertEqual(Solutiont153().findMin_4([2, 1]), 1)

    def test_lc154(self):
        from binary_search.LC154 import SolutionT154
        self.assertEqual(SolutionT154().findMin_2([2, 2, 2, 0, 1]), 0)
        self.assertEqual(SolutionT154().findMin_2([3, 1, 1]), 1)
