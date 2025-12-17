def twosum(nums):##brute force solution
    target = 13
    n = len(nums)
    lis = []

    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if nums[i] + nums[j] == target:
                lis.append([nums[i], nums[j]])
            j += 1
        i += 1

    return lis



nums=[5,9,1,2,4,15,6,3]
target=13
print(twosum(nums))


##optimal solution

def opti(nums,target):
    n=len(nums)
    hash_map={}
    for i in range(0,n):
        remaining =target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        else:
            hash_map[nums[i]]=i
    return hash_map
        
print(opti(nums,target))
