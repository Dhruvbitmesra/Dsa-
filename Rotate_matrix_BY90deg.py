mat=[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,15]]

row=len(mat)
col=len(mat[0])
result=[[0 for _ in range(row)]for _ in range(row)]
def rot(mat,row,result):
    for i in range(0,row):
        for j in range (0,row):
            result[j][(row-1)-i]=mat[i][j]
    
    return result
        


print(rot(mat,row,result))



##optimal solution

def opti(mat,row):
    for i in range(0,row-1):
        for j in range(i+1,row):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
    for j in range(0,row):
        mat[j].reverse()



        

