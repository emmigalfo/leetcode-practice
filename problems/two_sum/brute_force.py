class BruteForceSolution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #to avoid using the same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []