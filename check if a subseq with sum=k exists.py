def backtrack(k,index,total,subset,nums):
    result=[]
    if total==k:
        result.append(subset.copy())
        return True
    elif total>k:return False
    if index>=len(nums):return False
    subset.append(nums[index])
    sum=total+nums[index]
    pick=backtrack(index+1,sum,subset)
    if pick==True:return True
    subset.pop()
    sum=total
    not_pick=backtrack(index+1,sum,subset)
    return not_pick

