def Tower(n,beg,aux,end):
    if n==1:
        print("%c to %c"%(beg,end))
    else:
        Tower(n-1,beg,end,aux)
        Tower(1,beg,aux,end)
        Tower(n-1,aux,beg,end)


n=int(input("Enter the number of disk:"))
Tower(n,'A','B','E')
