import datetime as dt
today_date=dt.date.today()
print ("today only date is ", today_date)
print ("today is ", dt.datetime.today())
print (" date format ", dt.date(2023, 12, 2))
print (" time format ", dt.time(23, 12, 2))
print ("corrent time = ",dt.datetime.now())
#create datetime object
my_dateTime=dt.datetime(2025, 10,30, 13,40,50)
print(my_dateTime)
one_week= dt.timedelta(weeks=1)
next_week= today_date+ one_week
print("next_week = ",next_week)
print (" difference = ",dt.datetime(2023,12,1) - dt.datetime(2024,12,31))
print("String to date Object ",dt.datetime.strptime('2024-12-30 11.40.02'),"%Y-%m-%d %H:%M:%S")
print("date object to string format ",dt.datetime.strptime('2024-12-30 11.40.02'),"%Y-%m-%d %H:%M:%S")