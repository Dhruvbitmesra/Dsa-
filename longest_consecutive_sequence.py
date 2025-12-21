nums=[1,99,101,98,2,5,3,100]

def brute(nums):
    n=len(nums)
    max_count=0
    for i in range(0,n):
        num=nums[i]
        count=1
        while num+1 in nums:
            count+=1
            num=num+1
        max_count=max(max_count,count)
    return max_count


def better(nums):
    nums.sort()
    last_smaller=float('-inf')
    count=0
    n=len(nums)
    longest=0
    for i in range(0,n):
        num=nums[i]
        if num-1==last_smaller:
            count+=1
            last_smaller=num
        elif num-1!=last_smaller:
            count=1
            last_smaller=num
        longest=max(longest,count)
    return longest


def optimal(nums):
    if len(nums) == 0:
        return 0

    my_set = set(nums)
    longest = 0

    for num in my_set:
        # start counting only if num is the start of a sequence
        if num - 1 not in my_set:
            x = num
            count = 1

            while x + 1 in my_set:
                x += 1
                count += 1

            longest = max(longest, count)

    return longest


nums=[1,99,101,98,2,5,3,100]

print(brute(nums))
print(better(nums))
print(optimal(nums))

        


