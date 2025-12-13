nums = [55, 32, -97, 99, 3, 67]
##method 1
def giveno(nums):
    n = len(nums)
    largest = nums[0]
    i = 0

    while i < n:
        if nums[i] > largest:
            largest = nums[i]
        i += 1

    return largest

##print(giveno(nums))


##method 2
def largerfind(nums):
    largest=nums[0]
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i])
    return largest


print(largerfind(nums))
