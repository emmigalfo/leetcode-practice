import pytest
from problems.add_two_numbers.optimized import Solution as OptimizedSolution, ListNode
from problems.add_two_numbers.first_attempt import Solution as FirstAttemptSolution

def list_to_linked(lst):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_to_list(node):
    """Helper function to convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
        ([0], [0], [0]),  # Edge case: both zero
        ([9, 9, 9], [1], [0, 0, 0, 1]),  # 999 + 1 = 1000
        ([5], [5], [0, 1]),  # 5 + 5 = 10
        ([1, 8], [0], [1, 8]),  # 81 + 0 = 81
    ]
)
def test_add_two_numbers(l1, l2, expected):
    linked_l1 = list_to_linked(l1)
    linked_l2 = list_to_linked(l2)

    # Test First Attempt Solution
    first_attempt_sol = FirstAttemptSolution()
    first_attempt_result = first_attempt_sol.addTwoNumbers(linked_l1, linked_l2)
    assert linked_to_list(first_attempt_result) == expected, "First attempt solution failed"

    # Test Optimized Solution
    optimized_sol = OptimizedSolution()
    optimized_result = optimized_sol.addTwoNumbers(linked_l1, linked_l2)
    assert linked_to_list(optimized_result) == expected, "Optimized solution failed"

