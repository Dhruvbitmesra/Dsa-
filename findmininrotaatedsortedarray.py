##brute force approach
def finding(nums):
    min=float("inf")
    n=len(nums)
    for i in range(0,n):
        if nums[i]<=min:
            min=nums[i]
    
    return min



nums=[4,5,6,7,0,1,2]

print(finding(nums))


##find with optimal approach

def opti(nums):
    n=len(nums)
    mini=float("inf")
    high=n-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1

        else:
            mini=min(mini,nums[low])
            low=mid+1

    return mini



print(opti(nums))
