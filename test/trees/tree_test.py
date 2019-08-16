import unittest
import logging

from test.trees.trees import template_preorder_by_loop, template_preorder_iteratively, template_preorder_iterative_hf, \
                             template_inorder_by_loop, template_inorder_iteratively, \
                             template_postorder_by_loop, template_postorder_iteratively, template_postorder_iterative_hf
from test.trees.trees import get_binary_tree, get_binary_tree_02, get_binary_tree_03, \
    get_symmetric_tree, get_flip_equivalent_tree_a, get_flip_equivalent_tree_b
from test.trees.trees import get_multi_children_tree, get_subtree_a, get_subtree_b, get_unival_tree, get_pruned_tree


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
        from trees.LC104 import SolutionT104
        self.assertEqual(SolutionT104().maxDepth(get_binary_tree()), 3)

    def test_lc111(self):
        from trees.LC111 import SolutionT111
        self.assertEqual(SolutionT111().minDepth(get_binary_tree()), 2)
        self.assertEqual(SolutionT111().minDepth(get_binary_tree_02()), 2)

    def test_lc112(self):
        from trees.LC112 import SolutionT112
        self.assertEqual(SolutionT112().hasPathSum(get_binary_tree_03(), 22), True)

    def test_lc100(self):
        from trees.LC100 import SolutionT100
        self.assertEqual(SolutionT100().isSameTree(get_binary_tree(), get_binary_tree()), True)
        self.assertEqual(SolutionT100().isSameTree(get_binary_tree(), get_binary_tree_02()), False)
        self.assertEqual(SolutionT100().isSameTree(get_binary_tree(), get_binary_tree_03()), False)

    def test_lc101(self):
        from trees.LC101 import SolutionT101
        self.assertEqual(SolutionT101().isSymmetric(get_symmetric_tree()), True)

    def test_lc951(self):
        from trees.LC951 import SolutionT951
        self.assertEqual(SolutionT951().flipEquiv(get_flip_equivalent_tree_a(), get_flip_equivalent_tree_b()), True)

    def test_lc589(self):
        from trees.LC589 import SolutionT589
        self.assertEqual(SolutionT589().preorder(get_multi_children_tree()), [1, 3, 5, 6, 2, 4])
        self.assertEqual(SolutionT589().preorder_recursively(get_multi_children_tree()), [1, 3, 5, 6, 2, 4])
        self.assertEqual(SolutionT589().preorder_loop(get_multi_children_tree()), [1, 3, 5, 6, 2, 4])

    def test_lc590(self):
        from trees.LC590 import SolutionT590
        self.assertEqual(SolutionT590().postorder(get_multi_children_tree()), [5, 6, 3, 2, 4, 1])
        self.assertEqual(SolutionT590().postorder_recursively(get_multi_children_tree()), [5, 6, 3, 2, 4, 1])
        self.assertEqual(SolutionT590().postorder_loop(get_multi_children_tree()), [5, 6, 3, 2, 4, 1])

    def test_lc110(self):
        from trees.LC110 import SolutionT110
        self.assertEqual(SolutionT110().isBalanced(get_symmetric_tree()), True)
        self.assertEqual(SolutionT110().isBalanced_(get_symmetric_tree()), True)

    def test_lc572(self):
        from trees.LC572 import SolutionT572
        self.assertEqual(SolutionT572().isSubtree(get_subtree_a(), get_subtree_b()), True)
        self.assertEqual(SolutionT572().isSubtree(get_subtree_a(negtive=True), get_subtree_b()), False)

    def test_lc965(self):
        from trees.LC965 import SolutionT965
        self.assertEqual(SolutionT965().isUnivalTree(get_unival_tree()), True)
        self.assertEqual(SolutionT965().isUnivalTree(get_unival_tree(negtive=True)), False)
        self.assertEqual(SolutionT965().isUnivalTree_recursively(get_unival_tree()), True)
        self.assertEqual(SolutionT965().isUnivalTree_recursively(get_unival_tree(negtive=True)), False)

    # def test_lc814(self):
    #     from trees.LC814 import SolutionT814
    #     self.assertEqual(SolutionT814().pruneTree(get_pruned_tree()), get_pruned_tree(pruned=True))

    def test_lc113(self):
        from trees.LC113 import SolutionT113
        self.assertEqual(SolutionT113().pathSum(get_pruned_tree(), 2), [[1, 0, 1], [1, 1]])
        # self.assertEqual(SolutionT113().pathSum_hh(get_pruned_tree(), 2), [[1, 0, 1], [1, 1]])


if __name__ == '__main__':
    unittest.main()
