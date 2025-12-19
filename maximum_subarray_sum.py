def maxmarr(nums):##my brute force approach
    n = len(nums)
    maximum_sum = float('-inf')
    max_sub_arr = []

    for i in range(n):
        for j in range(i, n):
            current_sum = sum(nums[i:j+1])
            if current_sum > maximum_sum:
                maximum_sum = current_sum
                max_sub_arr = nums[i:j+1]

    return max_sub_arr, maximum_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
z = maxmarr(nums)
print(z)



##kadane algorithm

def kadane(nums):
    n=len(nums)
    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total=total+nums[i]
        maxi=max(maxi,total)
        if total<0:
            total=0
    return maxi

print(kadane(nums))
   