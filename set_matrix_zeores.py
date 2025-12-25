mat=[[7,9,2,3],
     [20,8,0,10],
     [29,0,-10,5],
     [4,14,6,6]]


###optimal

def opti(mat):
    rows = len(mat)
    cols = len(mat[0])

    zero_pos = []

    # Step 1: collect all zero positions
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                zero_pos.append((i, j))

    # Step 2: zero rows and columns
    for (i, j) in zero_pos:
        for col in range(cols):
            mat[i][col] = 0
        for row in range(rows):
            mat[row][j] = 0

    return mat


print(opti(mat))


#########brute 2 

def markinf(mat,row,col):
    r=len(mat)
    c=len(mat[0])
    for i in range(0,r):
        if mat[i][col]!=0:
            mat[i][col]=float("inf")
    for j in range(0,c):
        if mat[row][j]!=0:
            mat[row][j]=float("inf")
    
def setzeroes(self,mat):
    r=len(mat)
    c=len(mat[0])
    for i in range(0,r):
        for j in range(0,c):
            if mat[i][j]==0:
                self.markinf(mat,i,j)
    
    for i in range(0,r):
        for j in range(0,c):
            if mat[i,j]==float('inf'):
                mat[i][j]=0







  