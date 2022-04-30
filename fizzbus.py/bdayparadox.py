

# year= random.randint(1993,2022)

# print(year)

# if(year%4 == 0 and year%400 and year%100 != 0):
#     print(year,'is leap year')
# else:
#     print(year,'is not a leap year')

# import datetime
# birthday =[]
# i=0
# while(i<50):
#     year= random.randint(1895,2022)
#     if(year%4 == 0 and year%400 == 0 and year%100 != 0):
#         leap=1
#     else:
#         leap=0
#     month = random.randint(1,12)
#     if(month == 2 and leap == 1):
#         day = random.randint(1,29)
#     elif(month== 2 and leap == 0):
#         day = random.randint(1,28)
#     elif(month == 7 and month == 8):
#         day = random.randint(1,31)
#     elif(month %2 == 0 and month > 7 and month < 12):
#         day = random.randint(1,31)
#     else:
#         day = random.randint(1,30)

#     dd = datetime.date(year,month,day)
#     day_of_year = dd.timetuple().tm_year
#     i=i+1
#     birthday.append(day_of_year)
# birthday.sort()              
# print(birthday)
import datetime

print(datetime.date.today())
# to display only year
print(datetime.date.today().strftime("%y"))
#to print particular month
print(datetime.date.today().strftime("%m"))
#to print particular day
print(datetime.date.today().strftime("%d"))
# week number of the year 
print(datetime.date.today().strftime("%W"))
#weekday of week
print(datetime.date.today().strftime("%w"))
#day fo yaer
print(datetime.date.today().strftime("%j"))
#day fonweek
print(datetime.date.today().strftime("%A"))
#3current time
print(datetime.datetime.now())

