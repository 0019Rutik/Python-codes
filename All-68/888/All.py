# list1 = [["Harry",1], ["carry", 34],["Marry", 76],["larry",76]]



# dict1= dict(list1)
# for item, value in dict1.items():
#     print(item ," ", value)
# #print(list1[0])
# python allows multiple values to assign 
# x, y, z = "Orange", "Banana", "pink"

# print(x)
# print(y)
# print(z)

# you can also assign same value to multiple variables

# a =b= c = "orange"
# print(a)
# print(b)
# print(c)

# x= "python"
# # y = "is"
# # z= "awesome"

# # int a
# # print(a * 5)
# print(type(x))

# a = "hallo i was busy with the next batalians"
# if "batalians"  in a:
#     print(a.upper())
#     print(a.lower())
#     print(a.strip())
#     print(a.replace("s", "j"))
#     print(a.split(";"))


#     <========== List =====>






# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackberry"
# thislist.insert(2,"dingo")
# thislist.append("butterfly")
# #print(thislist)
# tropical = ["hallo", "tan", " i ", "am ","here", "for ","you"]
# thislist.extend(tropical)
# #print(thislist)
# # 
# i =0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

# fruits = ["Apple", "banana", "Manngo","Kiwi","cherry"]
# digits = [23,45,23,54,67,76]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)
# 


# fruits.sort(key = str.lower )

# print(fruits)

#mylist = fruits.copy()

# list3 = fruits + digits

# print(list3)

# #print(mylist)
# for x in list3:
#     fruits.append(x)

# print(fruits)
# x =  ("apple","banana", "cherry")
# y = list(x)
# y[1] = "mango"

# x = tuple(y)
# print(x)

# unpacking a Tuple

# fruits =(1,23,44,56,78,65,43,45,6,78,23,3,3,3,3,3)

# # (green , yellow, *pink) = fruits

# # print(green)
# # print(yellow)
# # print(pink
# x = fruits.index(3)
# print(x)

from pprint import pprint
from re import M


myset = {"apple","banana","cherry","apple"}
# print(len(myset))
# set1= {"abc",34, True , 40, "male"}
# print(type(set1))
# thisset = set(("apple","banana","cherry"))
# print(thisset)


# tropical ={"pinnaple","manoali","masaba","apple"}
# list = [3,45,567,454,34,65,76]

# myset.update(list)
# #print(myset)
# #(myset.union(tropical))
# # z = myset.intersection(tropical)
# # print(z)
# z = myset.symmetric_difference(tropical)
# print(z)

#   <========= Dictionaries ===========>
# dictionaries use to store data in the fornm of key and values
# thisdict = { 
#     "brand":"Ford",
#     "model1":"Mustang",     
#     "year":1996,
#     "colors":["red", "white","blue"]
#   }
# chengeble but duplicate not allows
# print(thisdict["brand"])
# print(len(thisdict))
# print(type(thisdict))

# x = thisdict["model1"]
# print(x)
# for x in thisdict:
#     a = input("enter the key")
#     p = thisdict.get("input")
#     print(p)
# x = thisdict.keys()
# print(x)
# thisdict["height"] = "1998cm"
# print(x)
# x = thisdict.values()
# print(x)

# thisdict = { 
#     "brand":"Ford",
#     "model1":"Mustang",
#     "year":1996,    
#      "colors":["red", "white","blue"]
#  }
# x = thisdict.items()
# print(x)
# thisdict["year"] = 1999
# print(thisdict)
# a = input("Enter Your Key")

# if "a" in  thisdict:
#     x = thisdict.get("a")
#     print(a)

# for x in thisdict:
#     a= input("Enter Your Keys")
#     print(thisdict[a])
# for x in thisdict.values():
#     print(x)
# for x , y in thisdict.items():
#     print(x ,y)

# mydict = thisdict.copy()
# print(mydict)

# mydict2 = dict(mydict) 
# print(mydict2)
# child1 = {
#         "name": "Email",
#         "year":"2004"
#     }
# child2 = {
#         "name":"tan",
#         "age":22
#     },
# child3 = {
#         "name": "bhavi",
#         "age": 23
#     }
 
# myFamily = {
#     "child1": child1,
#     "child2": child2,
#     "child3": child3
# }

# print(myFamily)



# a = 33457 
# b = 200
# c = 92597

# # if b > a:
# #     print("B is bigger than a")
# # elif a > b:
# #     print("a id greater than b")

# if a > b or c > a:
#     print("Both conditions are True")

# i = 1
# while i < 6:
#     print(i)
#     if i == 18:
#         continue
#     print(i)
#     i = i+1

# adj = ["red","big","tasty"]

# fruits = ["apple","banana","cherry"]

# for x  in adj:
#     for y in fruits:
#         print(x , y)
    
#  to pass no of argumentts in function...use *

# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple","banana","cherry"]

# my_function(fruits)
# Recursion

# ///////////
#cars = ["Ford","Volvo","BMW"]
# class person:
#     def __init__(self, name,  age):
#         self.name = name
#         self.age = age

#     def myfun(self):
#         print("Hello my name is" + self.name)

# p1 = person("John",36)
# p1.myfun()
# ineritance allow us to define a class that inherits all the methods and properties from anothher class .


# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname


#     def printname(self):
#         print(self.firstname , self.lastname)

# # use the class person to create object and the execute  the printname method
# class student(person):
#     def __init__(self,fname,lname,year):

#        super().__init__( fname, lname)
#        self.graduationyear = year

# x = student("John","Doe",2019)
# print(x.graduationyear)
# ioterators 

# mystr  = "banana"
# myit = iter(mystr)


# def hallo():
#     print("3")

# quantity = 30
# itemo = 567
# price= 49

# myorder ="I want {0} prices of item nummber  {1} for {2:.2f} dollers"
# print(myorder.format(quantity , itemo , price))

#==============> File Hhandlinng in python <=============

f =  open("/pythonfile/fizzbus.py/",'r')
print(f.read())

