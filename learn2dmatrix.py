nums=[[5,20,3],
      [7,-10,9],
      [1,-52,6]]
rows=len(nums)
cols=len(nums[0])
for i in range(0,rows):
    for j in range(0,cols):
        if i>=j:
            print(nums[i][j],end=" ")
        else:
            print("*")

for i in range(0,rows):
    for j in range(0,cols):
        if i==j:
            print(nums[i][j],end=" ")
        else:
            print("*")
