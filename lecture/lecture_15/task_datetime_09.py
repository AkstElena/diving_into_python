from datetime import datetime, timedelta

d = datetime.now()
td = timedelta(hours=1)
for i in range(24 * 7):
    if d.weekday() == 6:
        break
    else:
        d = d + td
print(i)
