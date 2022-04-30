from msilib.schema import Binary


def binary(L,x,start,end):
    mid = int((start+end)/2)
     
    if(start  == end):
        if(L[end] == x):
            return end
        else:
            return -100


    if(L[mid] == x):
        return mid
    elif(x>L[mid]):
        return Binary(L,x,mid+1,end) 
    else:
        return Binary(L,x,start,mid-1) 


L =[1,2,3,4,5,6,7,8]
x =input('enter the value')
print(binary(L,x,0,len(L)-1))
index = binary(L,x,0,len(L)-1)
if(index == -1):
    print(x,'not found')
elif(index == 0):
    print('not found')
else:
    print(x,'is found at position' ,index+1)