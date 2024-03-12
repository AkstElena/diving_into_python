from datetime import time, date, datetime, timedelta

t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
              microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)
print(f'{new_dt}\n{one_more_hour}')
