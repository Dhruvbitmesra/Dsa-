def backtrack(k,index,total,subset,nums):
    result=[]
    if total==k:
        result.append(subset.copy())
        return
    elif total>k:
        return
    if index>=len(nums):
        return
    subset.appen(nums[index])
    sum=total+nums[index]
    backtrack(index+1,sum,subset)
    subset.pop()
    sum=total
    backtrack(index+1,subset,sum)

