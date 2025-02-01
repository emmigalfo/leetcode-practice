import unittest
from brute_force import BruteForceSolution
from hash_map import HashMapSolution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.brute_force = BruteForceSolution()
        self.hash_map = HashMapSolution()

    def test_cases(self):
        test_cases = [
            ([2,7,11,15], 9, [0,1]),
            ([3,2,4], 6, [1,2]),
            ([3,3], 6, [0,1]),
        ]

        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target):
                self.assertEqual(self.brute_force.twoSum(nums, target), expected)
                self.assertEqual(self.hash_map.twoSum(nums, target), expected)

if __name__ == "__main__":
    unittest.main()
