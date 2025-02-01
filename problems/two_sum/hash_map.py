class HashMapSolution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index, i]
            num_to_index[num] = i
        return []