# one line function
# from ast import Lambda
# x=5 
# y=5

# minus = Lambda x,y:x-y
# print(minus)

# me = "Harry"

# a = f"This is %s"%me
# print(a)

# me ="harry"
# a1 = 3

# # a= "This is {1}  {0}"
# # b = a.format(me,a1)
# a = f"this is {me} {a1}  {Math.cos(65)}"


# print(a)

def funargs(*args):
    for item in args:
        print(item)

har = ["harry","rock","andy","dev","shubham","radhe"]
funargs(*har)