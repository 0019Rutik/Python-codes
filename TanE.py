print("Enter Your First Number?")
num1 =( input())
print("Enter Your Second Number")
num2 = (input())
try:
    print("The sum of the number is ",int(num1)+  int(num2))
except Exception as e:
    print(e)

print("This line is very important!")