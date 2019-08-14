import unittest
import logging

from trees.LC104 import SolutionT104
from trees.LC111 import SolutionT111
from trees.LC112 import SolutionT112
from trees.LC100 import SolutionT100
from trees.LC101 import SolutionT101
from trees.LC951 import SolutionT951
from test.trees.trees import get_binary_tree, get_binary_tree_02, get_binary_tree_03, \
    get_symmetric_tree, get_flip_equivalent_tree_a, get_flip_equivalent_tree_b


class TreeTest(unittest.TestCase):
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
