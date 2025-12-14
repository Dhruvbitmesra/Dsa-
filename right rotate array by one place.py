##1 method is by slicing only valid for python

nums = [5, -2, 3, 9, 0, 6, 10, 7]
n = len(nums)

nums[:] = [nums[n-1]] + nums[0:n-1]

print(nums)


##2 method is by when slicing is not involved

nums1 = [5, -2, 3, 9, 0, 6, 10, 7]

temp=nums1[n-1]
for i in range(n-2,-1,-1):
    nums1[i+1]=nums1[i]
nums1[0]=temp

print(nums1)