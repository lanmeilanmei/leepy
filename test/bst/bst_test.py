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
