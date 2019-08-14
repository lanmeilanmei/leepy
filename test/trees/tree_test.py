import unittest
import logging

from test.trees.trees import template_preorder_by_loop, template_preorder_iteratively, template_preorder_iterative_hf, \
                             template_inorder_by_loop, template_inorder_iteratively, \
                             template_postorder_by_loop, template_postorder_iteratively, template_postorder_iterative_hf
from test.trees.trees import get_binary_tree, get_binary_tree_02, get_binary_tree_03, \
    get_symmetric_tree, get_flip_equivalent_tree_a, get_flip_equivalent_tree_b
from trees.LC104 import SolutionT104
from trees.LC111 import SolutionT111
from trees.LC112 import SolutionT112
from trees.LC100 import SolutionT100
from trees.LC101 import SolutionT101
from trees.LC951 import SolutionT951


class TreeTest(unittest.TestCase):
    def test_preorder(self):
        self.assertEqual(template_preorder_by_loop(get_binary_tree()), [3, 9, 20, 15, 7])
        self.assertEqual(template_preorder_iteratively(get_binary_tree()), [3, 9, 20, 15, 7])
        self.assertEqual(template_preorder_iterative_hf(get_binary_tree()), [3, 9, 20, 15, 7])

    def test_inorder(self):
        self.assertEqual(template_inorder_by_loop(get_binary_tree()), [9, 3, 15, 20, 7])
        self.assertEqual(template_inorder_iteratively(get_binary_tree()), [9, 3, 15, 20, 7])

    def test_postorder(self):
        self.assertEqual(template_postorder_by_loop(get_binary_tree()), [9, 15, 7, 20, 3])
        self.assertEqual(template_postorder_iteratively(get_binary_tree()), [9, 15, 7, 20, 3])
        self.assertEqual(template_postorder_iterative_hf(get_binary_tree()), [9, 15, 7, 20, 3])

    def test_lc104(self):
        self.assertEqual(SolutionT104().maxDepth(get_binary_tree()), 3)

    def test_lc111(self):
        self.assertEqual(SolutionT111().minDepth(get_binary_tree()), 2)
        self.assertEqual(SolutionT111().minDepth(get_binary_tree_02()), 2)

    def test_lc112(self):
        self.assertEqual(SolutionT112().hasPathSum(get_binary_tree_03(), 22), True)

    def test_lc100(self):
        self.assertEqual(SolutionT100().isSameTree(get_binary_tree(), get_binary_tree()), True)
        self.assertEqual(SolutionT100().isSameTree(get_binary_tree(), get_binary_tree_02()), False)
        self.assertEqual(SolutionT100().isSameTree(get_binary_tree(), get_binary_tree_03()), False)

    def test_lc101(self):
        self.assertEqual(SolutionT101().isSymmetric(get_symmetric_tree()), True)

    def test_lc951(self):
        self.assertEqual(SolutionT951().flipEquiv(get_flip_equivalent_tree_a(), get_flip_equivalent_tree_b()), True)


if __name__ == '__main__':
    unittest.main()
