def insert(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1

        # Shift elements to the right
        while j >= 0 and nums[j] < key:
            nums[j+1] = nums[j]
            j -= 1

        # Insert key at correct position
        nums[j+1] = key
    
    return nums


nums = [3,5,6,4,8,7,10,1,9]
z = insert(nums)
print(z)
