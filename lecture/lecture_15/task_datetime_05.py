from datetime import time, date, datetime, timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
              microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101,
                  seconds=303, milliseconds=60)
print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')
