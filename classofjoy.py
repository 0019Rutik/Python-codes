# L= [1,2,3,4,5]

# n = len(L)
# for i in range(-1,-n-1,-1):
#     print(L[i])

def recursion(x,n):
    if (n == 0):
        return 1
    if(x == 1):
        return x
    
    return x * recursion(x,n-1)

print(recursion(2,5))