import time
from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
# дефолтные значения формируются один раз и потом запоминаются и не изменяются
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
time.sleep(7)
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
