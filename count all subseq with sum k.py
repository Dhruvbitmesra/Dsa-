def backtrack(index,total,k,nums):
    count=0
    if total==k:
       return 1
    elif total>k:
        return 0
    if index>=len(nums):
        return 0
    sum=total+nums[index]
    pick=backtrack(index+1,sum)
    sum=total
    not_pick=backtrack(index+1,sum)
    return pick+not_pick


