import time
import sys
from problems.two_sum.brute_force import BruteForceSolution
from problems.two_sum.hash_map import HashMapSolution

# Test cases
test_cases = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 1000, 19),  # Large case
]

def benchmark(solution, name):
    print(f"Testing {name} Solution...")
    solver = solution()
    
    for nums, target in test_cases:
        start = time.time()
        result = solver.twoSum(nums, target)
        end = time.time()
        print(f"Input: {nums[:5]}... (len={len(nums)}) | Output: {result} | Time: {end - start:.6f}s")
    print("\n")

if __name__ == "__main__":
    benchmark(BruteForceSolution, "Brute Force")
    benchmark(HashMapSolution, "Hash Map")
