import datetime as dt  # alias
from datetime import datetime, date

today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)

print(dir(dt))

today = dt.date.today()
print(today)

know = now + dt.timedelta(hours=9)
print(know)

time_diff = know - now
print(time_diff)

xmas1 = datetime(2023, 12, 25, 0, 0, 0)
print(xmas1)

xmas2 = date(2023, 12, 25)
print(xmas2)
