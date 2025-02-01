# Two Sum Problem (LeetCode #1)

## Problem Statement
Given an array `nums` and an integer `target`, return indices of two numbers that add up to `target`.

### Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]


**
## Solution
I tried two solutions. 
* The first is a brute force solution using nested loops. This works but has a time complexity of O(n^2), so it is not ideal for large data sets.
* The second is a hash map (python dictionary). This one is faster because it reduces redundant comparisons. It has a time complexity of O(n). 