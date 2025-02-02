import time
from problems.add_two_numbers.first_attempt import Solution as FirstAttemptSolution, ListNode
from problems.add_two_numbers.optimized import Solution as OptimizedSolution

def list_to_linked(lst):
    """Convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Define test cases for this specific problem
test_cases = [
    ([2, 4, 3], [5, 6, 4]),  # 342 + 465 = 807
    ([0], [0]),  # 0 + 0 = 0
    ([9, 9, 9], [1]),  # 999 + 1 = 1000
    ([1, 8], [0]),  # 81 + 0 = 81
]

def benchmark(solution, name):
    """Run benchmarks for a specific solution."""
    print(f"Benchmarking {name} Solution...")
    solver = solution()

    for l1, l2 in test_cases:
        linked_l1, linked_l2 = list_to_linked(l1), list_to_linked(l2)

        start = time.time()
        result = solver.addTwoNumbers(linked_l1, linked_l2)
        end = time.time()

        output = linked_to_list(result)
        print(f"Input: {l1} + {l2} | Output: {output} | Time: {end - start:.6f}s")
    print("\n")

if __name__ == "__main__":
    benchmark(FirstAttemptSolution, "First Attempt")
    benchmark(OptimizedSolution, "Optimized")
