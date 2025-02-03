def check(nums):
    min_num = min(nums)
    new_list = []
    counter = 0
    # set counter
    for i, num in enumerate(nums):
        if num == min_num:
            counter = i
    # set new list
    for i in range(counter,len(nums)):
        new_list.append(nums[i])
    for i in range(0, counter):
        new_list.append(nums[i])
    # check if list is sorted 
    for i, num in enumerate(new_list):
        if i != 0:
            if new_list[i]<new_list[i-1]:
                return False
    return True
