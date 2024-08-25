import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()
print(now.year)
print(day_of_week)


date_of_birth = dt.datetime(year=2002, month=10, day=25)
print(date_of_birth)