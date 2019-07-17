def a(m,n):
    if(m==0):
        return n+1
    elif(m!=0 and n!=0):
        return a(m-1,a(m,n-1))
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
for i in range(0,m):
    for j in range(0,n):
        print("result a(%d %d),%d"%(i,j,a(i,j)))
