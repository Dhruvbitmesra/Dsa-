##swap two numbers
##a=5,b=10 ====> a=10,b=5 with help of xor operator
##if we xor two same no we get 0
##if we xor one no with zero we get same no 

a=5
b=10

a=a^b
b=a^b
a=a^b
print(a,b)

#-----------------------------------------------
##check if the ith bit is set or not i.e 1 at i posintion so true else false
##done by left shift or right shift
n=13
i=1
if(n&(1<<i))!=0:
    print(True)
else:
    print(False)

##right shft
if((n>>i)&1)!=0:
    print(True)
else:
    print(False)

#------------------------------------------------------------------------------------
##set the ith bit
##1)brute force soltution tc->logn
##we can do by converting n to bit and then traverse till i postion and if we get 0 then replace there 1 and if 1 exist keep at is
##2)optimal in o(1)

n1=9
i1=2
print(n1 | (1<<i1))

##clear the ith bit

n2=13
i2=2
print(n2^(1<<i2))##this is not right approach can run by conicidende

##2 approach
print(n2&~(1<<i2))


#----------------------------------------------------------------------------
##toggle the ith bit
print(n2^(1<<i2))##here it works  

##--------------------------------------------------------------------------------
##remove the right most bit
k=40
print(k&k-1)
##------------------------------------------------------------------------------------
##check if the number is power of 2 or not
k1=63
if (k1&k1-1)==0:
    print("yess")
else:
    print("no")
