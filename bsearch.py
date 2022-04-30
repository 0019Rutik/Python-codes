def binary_search(l,x,start,end):
    if(start == end):
        if(l[start]  == x):
            return start
        else:
            return  -1
    else:
        mid = int((start + end)/2)
        if(l[mid] == x):
            return mid
        elif (l[mid]>x):
            return binary_search(l,x,start,mid-1)
        else:
            return binary_search(l,x,mid+1,end)



l =  [12,23,20,75,74]
x =int(input('Enter the Right input'))
index = binary_search(l,x,0,len(l)-1)
if(index == -1):
    print(x,'not found')
elif(index == 0):
    print('not found')
else:
    print(x,'is found at position' ,index+1)