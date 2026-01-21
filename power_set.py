def sub(nums):
    n = len(nums)
    total_subsets = 1 << n
    result = []

    for mask in range(total_subsets):
        lst = []
        for i in range(n):
            if mask & (1 << i) != 0:
                lst.append(nums[i])
        result.append(lst)

    return result



nums=[1,2,3]
print(sub(nums))