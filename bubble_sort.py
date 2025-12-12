def bubble(nums):
    is_swap=False
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        if is_swap==False:
            break
    return nums



n=[5,1,6,8,3,4,2,9,7]

v=bubble(n)

print(v)


