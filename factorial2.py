'''recursive version of the '''

'''
def factorial(n):
    product =1
    for i in range(1,n+1):
        product =product*i
    return product

n = int(input('enter positive values'))
if(n<0):
    print("Enter positive value only")
f = factorial(n)
print(f)
'''
'''Recursive Approach'''

def factorial(n):
    if(n == 0):
        return 1
    else:
        return  n*factorial(n-1)
    
n = int(input('enter positive values'))
if(n<0):
    print("Enter positive  value only")
f = factorial(n)
print('The factorial of Number ',n ,'is', f)