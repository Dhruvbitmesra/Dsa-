def solve(ind,subset):
    nums=[12,5]
    result=[]
    if ind>=len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[ind])
    solve(ind+1,subset)
    subset.pop()
    solve(ind+1,subset)
