def countocc(arr, target):
    n = len(arr)

    # -------- First Occurrence --------
    low, high = 0, n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1      # move left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # If target not found
    if first == -1:
        return 0

    # -------- Last Occurrence --------
    low, high = 0, n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1       # move right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last - first + 1



nums=[1,2,3,3,3,3,3,35,6,8,9,9,10] 
print(countocc(nums,3))