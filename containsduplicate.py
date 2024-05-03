def containsDuplicate(nums):
    # solution code here
    for index1 in range(0, len(nums)):
        for index2 in range(0, len(nums)):
            if index1 == index2:
                continue
            value1 = nums[index1]
            value2 = nums[index2]
            if value1 == value2: # Duplicate found
                return True
    
    return False
    # either return True or False
result =containsDuplicate()
print (result)