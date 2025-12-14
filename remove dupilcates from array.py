
##this method for sorted or unsorted array both
def remove_duplicates(nums):
    i = 0
    while i < len(nums):
        j = len(nums) - 1
        while j > i:
            if nums[i] == nums[j]:
                nums.pop(j)
            j -= 1
        i += 1
    return nums



###method with dict Brute force approach only for sorted arrays

def dct(nums):
    n=len(nums)
    freq_map={}
    for i in range(0,n):
        freq_map[nums[i]]=0
    j=0
    for k in freq_map:
        nums[j]=k
        j+=1

    return j

##optimal approach two adjacent pointers only for sorted arrays

def opt(nums):
    n = len(nums)
    if n == 0:
        return 0

    i = 0
    j = i + 1

    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    return i + 1




nums = [1,1,1,2,3,4,4,7,9,9,9,20]
print(opt(nums))



