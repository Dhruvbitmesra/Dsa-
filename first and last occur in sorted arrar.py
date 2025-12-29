def firstandlast(nums, target):
    n = len(nums)
    
    # ---------- First Occurrence ----------
    low, high = 0, n - 1
    first = -1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1   # move left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # ---------- Last Occurrence ----------
    low, high = 0, n - 1
    last = -1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1    # move right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first, last


nums = [1,2,3,3,3,3,5,6,8,9,9,10]
print(firstandlast(nums, 3))
