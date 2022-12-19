from datetime import date
import pandas as pd

def day_name_of_week(data):
    return data.day_name()

'''year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

if year >=10000 or month > 12 or day > 31:
    raise ValueError('The data is incorrect.')
if year % 4 != 0 and month == 2 and day > 28:
    raise ValueError('The day is incorrect.')
if year % 4 == 0 and month == 2 and day > 29:
    raise ValueError('The day is incorrect.')

d = date(year, month, day)
dat = pd.Timestamp(d)
#print(dat)
print(day_name_of_week(dat))'''