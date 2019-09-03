import unittest


class DPTest(unittest.TestCase):
    def test_lc746(self):
        from dynamic_programming.LC746 import Solutiont746
        self.assertEqual(Solutiont746().minCostClimbingStairs_4([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
        self.assertEqual(Solutiont746().minCostClimbingStairs_5([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
