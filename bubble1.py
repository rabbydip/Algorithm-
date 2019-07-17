def binary_search(sorted,length,key):
    start=0
    end=length-1
    while start<=end:
        mid=(int)((start+end)/2)
        if key==sorted[mid]:
            print(key,"is found",mid,"index")
            return-1
        elif key <sorted[mid]:
            end=mid-1
        elif key>sorted[mid]:
            start=mid+1


    print("failed the found:")
    return-1

array=[]
n=int(input("enter the array size:"))
print("Enter the element of array:")
for i in range(0,n):
    x=int(input())
    array.append(x)

print("this array:",array)
array.sort()
print("after the sorted",array)
p=int(input("search the item:"))
binary_search(array,n,p)
        
