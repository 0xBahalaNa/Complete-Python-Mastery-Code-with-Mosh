"""
9. Python Standard Library, 10. Working with DateTimes

datetime module and class.

https://docs.python.org/3/library/datetime.html

Documentation for working with datetime module.
"""
from datetime import datetime
import time

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year} /{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)
