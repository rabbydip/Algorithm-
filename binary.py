def binary_search(sorted_array,length,key):
    Start = 0
    end=length-1
    while Start<=end:
         mid =(int)((Start+end)/2)
         if key == sorted_array[mid]:
            print(key,"is found in",mid,"index")
            return-1

         elif key<sorted_array[mid]:
            end=mid-1

         elif key>sorted_array[mid]:
              Start=mid+1
        
    print("failed to found")
    return-1

array=[]
size=int(input("Enter the Size of array:"))
print("Enter the elements of array:")
for i in range(0,size):
    x=int(input())
    array.append(x)
print("The array is",array)
array.sort()
print("After sorting",array)
p=int(input("what you search:"))
binary_search(array,size,p)
