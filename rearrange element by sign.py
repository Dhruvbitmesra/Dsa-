def calculate(nums):##brute force solution
    pos = []
    neg = []

    for x in nums:
        if x < 0:
            neg.append(x)
        else:
            pos.append(x)

    return pos, neg


def re(pos, neg):
    nums = []
    n = min(len(pos), len(neg))  # safe length

    for i in range(n):
        nums.append(neg[i])
        nums.append(pos[i])

    # add remaining elements (if any)
    nums.extend(neg[n:])
    nums.extend(pos[n:])

    return nums


nums = [5, 10, -3, -1, -10, 6]
pos, neg = calculate(nums)
print(re(pos, neg))


def opti(nums):
    n=len(nums)
    result=[0]*n
    pos_index,neg_index=0,1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2
    return result

print(opti(nums))

