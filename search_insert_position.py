def search(nums):
    low = 0
    high = len(nums) - 1
    target = 2
    lb = len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
print(search(nums))
