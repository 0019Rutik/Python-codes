#current time
# from datetime import datetime as dt

# import datetime 

# from datetime import datetime as dt

# dt.now()

# print(dt.now())

# print(dt.now
# )


# print(dt.now(tz))

# print(len(pytz.all_timezones)
# 
import calendar

# yy = 2022

# mm = 4

# #display the calender 

# ca2  = calendar.month(yy,mm)

# print(ca2)
# print(calendar.weekday(2018,7,6))

# print(calendar.weekday(2022,4,11))

def check_leap(y):
    if(y % 100 == 0):
        if(y % 400 == 0):
            return True
        else:
            return False
    else:
        if(year % 4 == 0 ):
            return True

        else:
            return False

def check_valid_date(dt,m,y,l):
    if (l):
        if(m == 2):
            if(dt<30):
                return True
            else:
                return False
        else:
            if(m < 8):
                if(m % 2 == 1):
                    if(dt < 32):
                        return True
                    else:
                        return False
                else:
                    if(dt < 31):
                        return True
                    else:
                        return False
            else:
                if(m % 2 == 0 ):
                    if(dt < 32):
                        return True
                    else:
                        return False
                else:
                    if(dt < 31):
                        return True
                    else:
                        return False

    else:
        if(m == 2):
            if(dt<29):
                return True
            else:
                return False
        else:
            if(m < 8):
                if(m % 2 == 1):
                    if(dt < 32):
                        return True
                    else:
                        return False
                else:
                    if(dt < 31):
                        return True
                    else:
                        return False
            else:
                if(m % 2 == 0 ):
                    if(dt < 32):
                        return True
                    else:
                        return False
                else:
                    if(dt < 31):
                        return True
                    else:
                        return False
                


while(1):
    year = int(input('Enter Year From 1970 - 2022'))

    if(year < 1970):
        print("please Enter year in the range 1970")
    else:
        break

while(1):
    month = int(input('Enter month From (1-12)'))

    if(month <= 12 and month > 0):
        break
    
    else:
        print("please Enter Valid Month in the range 1-12")

leap = check_leap(year)
while(1):
    date = int(input('Enter date :'))

    if (date > 0) and (check_valid_date(date ,month , year, leap)):
        break
    
    else:
        print("please Enter Valid Month in the range 1-12")


    
        


