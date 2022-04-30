def fibonacii(n):
    if(n <1):
        return 1
    else:
        return n + fibonacii(n-1)
n =int(input('enter The Int'))
if(n <=0):
    print("enter the vaid values")

else:
    print(fibonacii(n))

