import datetime
import math

d = datetime.date(2024, 3, 16)  # Saturday
# print(d.replace(year=2023, day=29))
print(d.weekday())
print(d.isoweekday())

today = datetime.date.today()
print(type(d - today))

# date1 - date2 = timedelta
# date1 - timedelta = date2

# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)
# x = 1707412061
# print(tdelta.total_seconds())
#
# print(x - tdelta.total_seconds())
#
# t = datetime.time(18, 23, 42)
# print(t)
# t2 = datetime.time(23, 10, 32)

# dt = datetime.datetime(2024, 3, 16, 17, 12, 32)
# print(dt)
# tdelta = datetime.timedelta(hours=20)
# print(dt - tdelta)
# print((datetime.datetime.today() + tdelta).time())
# print(dt.timestamp())
# new_date = datetime.datetime.fromtimestamp(1710601952)
# print(new_date)

dt = datetime.datetime.today()
print(dt.strftime('%A****%d-----:::::: '))
date = 'Июль 12, 2023 18:22'
date = date.replace('Июль', 'July')
new_date = datetime.datetime.strptime(date, '%B %d, %Y %H:%M')
print(new_date)