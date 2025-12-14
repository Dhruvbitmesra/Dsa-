##better solution -> double path solution
def sec(nums):
    largest=float('-inf')
    s_largest=float('-inf')
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i])
    for i in range(0,n):
        if nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]

    return s_largest

##optimal solution -> single path solution

def second(nums):
    largest=float("-inf")
    s_largest=float("-inf")
    n=len(nums)

    for i in range(0,n):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
        
    return s_largest
    
    


nums=[55,32,97,-55,45,32,88,21]

sorted_array=second(nums)

print(sorted_array)