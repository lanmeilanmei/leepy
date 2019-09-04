import unittest


class DPTest(unittest.TestCase):
    def test_lc746(self):
        from dynamic_programming.LC746 import Solutiont746
        self.assertEqual(Solutiont746().minCostClimbingStairs_4([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
        self.assertEqual(Solutiont746().minCostClimbingStairs_5([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_lc198(self):
        from dynamic_programming.LC198 import SolutionT198
        self.assertEqual(SolutionT198().rob([2, 1, 1, 2]), 4)
        self.assertEqual(SolutionT198().rob_2([1, 2, 3, 1]), 4)
        self.assertEqual(SolutionT198().rob_2([2, 1, 1, 2]), 4)
        self.assertEqual(SolutionT198().rob_3([2, 1, 1, 2]), 4)
