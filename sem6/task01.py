import datetime


date_to_prove = '31.6.2022'

day, month, year = date_to_prove.split('.')
print(year, month, day)
try:
    datetime.datetime(int(year), int(month), int(day))
    print(1)
except Exception as e:
    print(0, e)