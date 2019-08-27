import unittest
from test.bst.bst import BSTtrees


class BSTtest(unittest.TestCase):
    def test_bst(self):
        self.assertEqual(BSTtrees().inorder(BSTtrees.bst_1()), [1, 2, 3])

    def test_lc98(self):
        from bst.LC98 import SolutionT98
        self.assertEqual(SolutionT98().isValidBST(BSTtrees.bst_1()), True)
        self.assertEqual(SolutionT98().isValidBST(BSTtrees.bst_1(negtive=False)), False)
        self.assertEqual(SolutionT98().isValidBST(BSTtrees.bst_2()), False)
        self.assertEqual(SolutionT98().isValidBST_Iteratively(BSTtrees.bst_2()), False)
        self.assertEqual(SolutionT98().isValidBST_Iteratively(BSTtrees.bst_1()), True)

    def test_lc530(self):
        from bst.LC530 import SolutionT530
        self.assertEqual(SolutionT530().getMinimumDifference(BSTtrees.bst_2(negtive=False)), 1)
        self.assertEqual(SolutionT530().getMinimumDifference_2(BSTtrees.bst_2(negtive=False)), 1)
        self.assertEqual(SolutionT530().getMinimumDifference_Iteratively(BSTtrees.bst_2(negtive=False)), 1)

    def test_lc230(self):
        from bst.LC230 import SolutionT230
        self.assertEqual(SolutionT230().kthSmallest(BSTtrees.bst_230(), 1), 1)
        self.assertEqual(SolutionT230().kthSmallest_2(BSTtrees.bst_230(), 1), 1)
        self.assertEqual(SolutionT230().kthSmallest_Iteratively(BSTtrees.bst_230(), 1), 1)

    def test_lc501(self):
        from bst.LC501 import SolutionT501
        self.assertEqual(SolutionT501().findMode(BSTtrees.bst_501()), [2])
        self.assertEqual(SolutionT501().findMode(BSTtrees.bst_501(extend=True)), [5, 6])
        self.assertEqual(SolutionT501().findMode_2(BSTtrees.bst_501(extend=True)), [5, 6])
