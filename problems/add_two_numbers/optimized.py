# Used AI to help find and learn about optimized solution (credit here goes to ChatGPT)
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            # Store the single digit in the new node
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next  # Skip dummy head and return actual result
