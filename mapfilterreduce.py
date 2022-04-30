# num = [2,3,4,5,6,7,8]
# # square = list(map(lambda x:x*x,num))
# # print(square)
# def sq(n):
#     return n*n

# square = list(map(sq,num))
# print(square)
from ast import Lambda
from functools import reduce


#<-----> filter -------->
# list_1 = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5,list_1))
# print(gr_than_5)

#<--------Reduce---------->
list_1 =[1,2,3,4,5,6]
num = reduce (Lambda x , y : x+y, list_1)
print(num)
