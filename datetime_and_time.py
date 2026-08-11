'''
datetime---->date,time module functionalities
time
'''
import datetime
print(dir(datetime))
from datetime import datetime,timedelta
'''a=datetime.now()#returns current time
print(a)
print(type(a))
#based on above datetime object we can extract separately as below
d=datetime.now()
print(d.date())
da=d.day
m=d.month
y=d.year
print(f'Today is {da}-{m}-{y}')
g=datetime.today()
print(g)
print(type(g))
h=g.weekday() #monday will be 0
print(h)
k=g.isoweekday()#in ISO sunday will be 0
print(k)
l=g.time()
print(l)
#stringformatting---->convert datetime to string
print(g.strftime('%W'))#number of days in this month
print(g.strftime("%m"))
print(g.strftime("%w"))
print(f'Today is {g.strftime("%A")}')'''

#we can create a datetime object
'''b=datetime(2026,8,15)
print(b)
c=datetime(day=16,month=9,year=2026,hour=10,minute=30)
print(c)
print(type(c))'''

#accept input from user---->convert to datatime object---->return 
'''day=int(input("enter the day:"))
month=int(input("enter the month:"))
year=int(input("enter the year:")) 
a=datetime(year,month,day)
print(a.strftime('%W'))
print(a.strftime("%m"))
print(a.strftime("%w"))
print(f'Today is {a.strftime("%A")}')
print(f'Today is {a.strftime("%B")}')'''
#strptime()-->stringpointoftime---->datetime---->str format
f=datetime.now()
print(f)
print(type(f))
dayofweek=datetime.strptime('26-12-1993',"%d-%m-%Y")
print(dayofweek)
#timedelta
#days,hours,minutes,secods

diff = timedelta(days=5,hours=10)
print(diff)

print(f-diff)
print(f+timedelta(hours=5,minutes=30))
d=f+timedelta(hours=5,minutes=30)
print(d)

import time
print(dir(time))
print(time.tzname)
print(time.ctime())#returns in string
d_obj=time.localtime()#returns in structure
y=d_obj.tm_year
month=d_obj.tm_mon
day=d_obj.tm_mday
print(f"Date is {day}-{month}-{y}")

