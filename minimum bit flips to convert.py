##flips the number
def flipping (start,goal):
    num=start^goal
    count=0
    for i in range(0,32):
        if num&(1<<i)!=0:
            count+=1
    return count




