# Add Two Numbers (Leetcode #2)

## Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

## Solution
My first failed attempt worked with python lists but not with listnode types (see notebook).

#### My Attempt
 My attempt worked by coverting the linked lists into regular python lists and then reversing, stringing, and joining and finally integering (i know that's not a real word) to create numbers out of the linked lists. I then sumed the two numbers and then turned that number into a linked list as a return value. It worked decent. 
    
-Lets talk about the __computational complexity__ of the first attempt:
Step 1: Extract values from linked lists (O(n) + O(m))
``` 
while l1:
    list1.append(str(l1.val))
    l1 = l1.next
while l2:
    list2.append(str(l2.val))
    l2 = l2.next
```
I iterate through l1 and l2 once each, appending values to lists.
If n is the length of l1 and m is the length of l2, this step takes O(n) + O(m).

Step 2: Reverse lists, convert to integers, and add (O(n) + O(m))
```
number1 = int(''.join(list1[::-1]))  
number2 = int(''.join(list2[::-1]))
sum_of_nums = number1 + number2
```
Reversing the list (list1[::-1] and list2[::-1]) takes O(n) + O(m).
Joining and converting to an integer (int(''.join(...))) takes O(n) + O(m) because:
String concatenation of n digits takes O(n).
The integer conversion takes O(n).
Addition (number1 + number2) is O(max(n, m)).
Thus, this step is O(n) + O(m).

Step 3: Convert sum back to a linked list (O(d))
```
sum_list = list(str(sum_of_nums))  
dummy_head = ListNode()
current = dummy_head

for num in reversed(sum_list):
    current.next = ListNode(int(num))
    current = current.next

```
String conversion (str(sum_of_nums)) takes O(d) where d is the number of digits in sum_of_nums. Since d ≈ max(n, m), we consider O(n) + O(m).
Creating the linked list takes O(d) ≈ O(n) + O(m).

Overall Complexity
Each step runs in O(n) + O(m), so the total time complexity is:

O(n)+O(m)

where:
n is the length of l1 (first linked list),
m is the length of l2 (second linked list).
Thus, your solution runs in linear time: O(n + m)

#### AI optimized solution

(see optimized.py)

__Avoid list conversions__

Instead of extracting values into lists and reversing them, traverse the linked lists backward using recursion or reverse the lists in place.
This eliminates the need for O(n) + O(m) space for storing numbers.

__Perform digit-wise addition directly on the linked lists__

Instead of converting to integers, sum digits on the fly, just like manual addition.
Use recursion to handle the addition from least significant digit (LSD) to most significant digit (MSD).

__Minimize extra memory__

The most memory-efficient way is to modify one of the input lists in-place, if allowed.
If modifying in-place isn’t allowed, construct a new linked list but avoid unnecessary temporary structures.

##### Why is this the most optimized?
__Time Complexity:__ O(n) + O(m) = O(max(n, m)) 
We traverse l1 and l2 once, performing O(1) operations per node.
No extra loops, no list reversals, and no conversions to integers.

__Space Complexity:__ O(1) (In-Place Modification Possible)
If allowed, we can modify l1 or l2 directly instead of creating a new list.
Otherwise, we only use a few extra pointers (dummy, current, carry), making the additional space O(1).

### Takeaway
"Chatgpt, what's my takeaway?"

"
### 1. **Big-O Complexity Isn’t Everything**
- Even though both solutions have **O(n) + O(m)** time complexity, hidden **constant factors** (like string operations, list reversals, and integer conversions) make a huge difference in real-world performance.

### 2. **Avoid Unnecessary Data Transformations**
- Your approach **extracts digits, reverses lists, converts to strings, then to integers, then back to strings, then to a linked list**—all unnecessary overhead.
- Instead, **process digits directly** from the linked list and construct the result **on-the-fly**.

### 3. **Think in Terms of Memory Efficiency**
- Your solution **stores numbers in lists and strings**, consuming extra space.
- The optimized solution **only uses pointers**, keeping space complexity **O(1)** if modifying `l1` or `l2` in-place.

### 4. **Leverage the Linked List Structure**
- Your solution treats linked lists **like arrays**, but linked lists are best processed **node by node**.
- Instead of converting them into another format, **work with them directly**.

---

## **TL;DR**
✅ **Direct digit-wise processing is better than list/string/integer conversion.**  
✅ **Reduce extra steps—process on-the-fly.**  
✅ **Think about constant factors, not just Big-O complexity.**  
✅ **Memory efficiency matters as much as time efficiency.**  

By applying these principles, **your future solutions will be leaner, faster, and more optimized! **
"


```
Benchmarking First Attempt Solution...
Input: [2, 4, 3] + [5, 6, 4] | Output: [7, 0, 8] | Time: 0.000025s
Input: [0] + [0] | Output: [0] | Time: 0.000005s
Input: [9, 9, 9] + [1] | Output: [0, 0, 0, 1] | Time: 0.000019s
Input: [1, 8] + [0] | Output: [1, 8] | Time: 0.000004s


Benchmarking Optimized Solution...
Input: [2, 4, 3] + [5, 6, 4] | Output: [7, 0, 8] | Time: 0.000005s
Input: [0] + [0] | Output: [0] | Time: 0.000002s
Input: [9, 9, 9] + [1] | Output: [0, 0, 0, 1] | Time: 0.000007s
Input: [1, 8] + [0] | Output: [1, 8] | Time: 0.000002s ```
