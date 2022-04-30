# class student():
#     pass

# harry = student()
# larry = student()


# harry.name = "Harry"
# harry.std = 12
# harry.section = 1


# print(harry.name)
# class Employee:
#     no_of_leaves = 8
#     pass

# harry = Employee()
# rohan = Employee()

# harry.name = "Harry"
# rohan.salary = 455
# harry.role = "Instructor"
# print(rohan.no_of_leaves)
# harry.no_of_leaves = 5
# print(harry.no_of_leaves)
# print(harry.__dict__)

class Employee:
    no_of_leaves = 8
    def __init__(self ,name ,salary, role):
        
        pass


harry = Employee("rahul" , "4000" , "Engineer")
rohan = Employee("jumbo" , 4999, " dancer")

print(harry.salary)


