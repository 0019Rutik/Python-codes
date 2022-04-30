from datetime import datetime as dt 
import pytz 
import calendar
# timezone = pytz.all_timezones
# for i in range(len(timezone)):
#     zone = timezone[i]
#     tz = pytz.timezone(zone)
#     print("current time at zone",zone ,"is",dt.now(tz))
# print(dt.now())

zone = pytz.all_timezones

for i in range(len(zone)):
    print(dt.now(pytz.timezone(zone[i])))
# day  = dt.today()


# month= 12
# year = 2021
# day = 10

# print(day.weekday(year,month,day))
year = 2015
# # ca2 = calendar(year)
# # print(ca2)

# print(calendar.calendar(year))

# print(calendar.isleap(year))
# time = dt.now()
# print(time.time())