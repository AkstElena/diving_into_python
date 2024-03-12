from datetime import timedelta

delta = timedelta(weeks=53, days=500, hours=73, minutes=101,
                  seconds=303, milliseconds=67890,
                  microseconds=1234567)
neg_delta = timedelta(days=-3, minutes=-42)
print(f'{delta = }\t-\t{delta}')
print(f'{neg_delta = }\t-\t{neg_delta}')
