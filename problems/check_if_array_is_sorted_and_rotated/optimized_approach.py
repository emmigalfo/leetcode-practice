def check(nums):
    descent = 0
    n = len(nums)
    for i in range(n):
        if nums[i]>nums[(i+1) % n]:
            descent += 1
            if descent > 1:
                return False
    return True