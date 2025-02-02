from typing import Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        # step 1: extract lists from linked lists
        list1, list2 = [], []

        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        
        # Step 2: Reverse the lists and convert to integers
        number1 = int(''.join(list1[::-1]))  
        number2 = int(''.join(list2[::-1]))

        sum_of_nums = number1 + number2  # Compute the sum

        # Step 3: Convert sum to linked list
        sum_list = list(str(sum_of_nums))  # Convert to list of digits

        dummy_head = ListNode()  # Dummy node
        current = dummy_head

        for num in reversed(sum_list):  # Iterate in reverse order
            current.next = ListNode(int(num))
            current = current.next

        return dummy_head.next  # Return head of the result list

        