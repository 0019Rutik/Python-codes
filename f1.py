class person:
    country ="india"

    def takebreak(self):
     print("i am breathing and tired...")

class Employee(person):
    company = 'honda'

    def getsalary(self):
     print(f"salary is {self.salary} ")
     
    def takebreak(self):
      print("i am an Employee so i am luckily breathing...")

class programmer(Employee):
    company = "fiverr"
   
   
    def getsalary(self):
       print("no salary to programmers")

p = person()
p.takebreak()
e = Employee()
e.takebreak()
e.company()



  
  
  
  
  
  
