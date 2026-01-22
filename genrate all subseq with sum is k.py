##brute force 
def solve(ind,susbset,target):
    nums=[5,3,2]
    result=[]
    if ind>=len(nums):
        if sum(susbset)==target:
            result.append(susbset.copy())
            return
    susbset.append(nums[ind])
    solve(ind+1,susbset)
    susbset.pop()
    solve(ind+1,susbset)


##optimal

def opti(index,total,subset,target):
    result=[]
    nums=[5,6,8]
    if total==target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if index>=len(nums):
        return
    subset.append(nums[index])
    sum=total+nums[index]
    solve(index+1,sum,subset)
    e=subset.pop()
    sum=sum-e
    solve(index+1,sum,subset)
    

