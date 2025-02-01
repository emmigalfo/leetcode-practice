from typing import List
class HashMapSolution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        num_to_index = {} # Dictionary to store the number and it's index

        for i, num in enumerate(nums):
            complement = target - num # The number we need to find

            if complement in num_to_index:
                return [num_to_index[complement], i] # Return the two indices 
            
            num_to_index[num] = i #store index of the current number
        
        return [] # In case no solution is found