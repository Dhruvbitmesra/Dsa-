##binary search iterative method

def bin(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            return mid
        
        elif nums[mid]<target:
            low=mid+1

        else:
            high=mid-1

    
    return -1


nums=[2,4,6,7,9,11,18,19]

target=6


print(bin(nums,target))


##recursive solution

def binrec(nums, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binrec(nums, mid + 1, high, target)

    else:
        return binrec(nums, low, mid - 1, target)


nums = [1, 3, 4, 6, 8, 10]
low = 0
high = len(nums) - 1
target = 6

print(binrec(nums, low, high, target))
