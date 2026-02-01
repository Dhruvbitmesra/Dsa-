def backtrack(nums,index,total,subset,result,n):
    if total==0:
        result.append(subset.copy())
        return
    if total<0:
        return
    if index>=len(nums):
        return
    for i in range(index,n):
        if i>index and nums[i]==nums[i-1]:
            continue
        subset.append(nums[i])
        sum=total-nums[i]
        backtrack(i+1,sum,nums,subset,result)
        subset.pop()