nums1=[1,1,1,2,4,6,7]
nums2=[1,2,4,6,7,8,9,10]

n=len(nums1)
m=len(nums2)

i=0
j=0
result=[]

while i<n and j<m:
    if nums1[i] < nums2[j]:
        if len(result)==0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    elif nums2[j] < nums1[i]:
        if len(result)==0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

    else:  # nums1[i] == nums2[j]
        if len(result)==0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
        j += 1

while i < n:
    if result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

while j < m:
    if result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)
