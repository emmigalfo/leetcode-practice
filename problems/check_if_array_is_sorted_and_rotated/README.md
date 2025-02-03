# Check if Array Is Sorted and Rotated (1752)

(See LeetCode problem number 1752 for the problem description and constraints.)

For this problem, my initial attempt was wild! (See `first_approach.py`.)  
When I do these problems, my first approach is always me going as fast as I can with no outside help—just my own knowledge and instincts. Then, after I get a working solution, I take the time to go learn things and come back with an optimized approach.  

In my first attempt, I wanted to find the minimum number, add it to a new list, and use that as a launching point. The idea was to break the original list into two parts—the part after the minimum value and the part before—and then join them into a new list. This was because I didn’t know how to handle circular indexing.  

Another chaotic thing I did in this approach was create the new list and then loop through it to check if each number was greater than the one before it, but I skipped the first index because I wasn’t sure how to deal with bounds. Haha the good news is it worked.   

## Complexity Analysis (First Approach)
- **Time Complexity:** O(n) (linear) – Not bad.  
- **Space Complexity:** O(n) – Because I created a new list.  
- **Overall:** It worked, but there was definitely room for improvement.

## The Optimized Approach  
After solving it my way first, I went back and learned how to handle circular indexing properly (see `optimized_approach.py`), and now I feel much better about my solution. I re-learned a few things, including that I shouldn’t be afraid to use modulus (`%`) in indexing:  

```
# check to see if num is less than the next number in line. Will also check the last number against the first. 
nums[i] <= nums[(i + 1) % n]
```


This allowed me to look at the next number in line, even if that meant wrapping back to index `0`. This is one of those things I know about but tend to forget when solving problems under pressure. That’s what I like about these LeetCode daily challenges—they refresh me on concepts that don’t come up often in my work but might be needed in an interview.

## Complexity Analysis (Optimized Approach)
The optimized solution loops through the list once, counting how many times the numbers descend instead of ascend (which should be exactly **once** for a valid rotated sorted array).  

- **Time Complexity:** O(n) – One loop through the array.  
- **Space Complexity:** O(1) – No additional data structures needed.  

Well, I’m pretty happy with this final solution.
