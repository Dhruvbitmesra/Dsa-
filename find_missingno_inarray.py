def missno(arr,k):
    n=len(arr)
    key=k
    for i in range(0,n+1):
        if arr[i]==k:
            print(k)
  
    print(-1)





##optimal
def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual


k=4
arr=[1,5,2,3,6,7,7,8,8,9]

print(missingNumber(arr))