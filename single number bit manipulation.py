##brute force 
def find(nums):
    myset = set()
    
    for i in range(len(nums)):
        if nums[i] not in myset:
            myset.add(nums[i])
        else:
            myset.remove(nums[i])
    
    return myset.pop()

##optimal using bit manipulation

def bit(nums):
    ans=0
    for num in nums:
        ans=ans^num

    return ans


nums=[5,4,3,4,2,2,3]

print(bit(nums))
print(find(nums))