
from datetime import datetime, timedelta

dt_now = datetime.now()
day = timedelta(1)
dt_yesterday = dt_now - day
dt_30_days_ago = dt_now - day*30

str_yesterday = dt_yesterday.strftime('%Y-%m-%d')
str_now = dt_now.strftime('%Y-%m-%d')
str_30_days_ago = dt_30_days_ago.strftime('%Y-%m-%d')
print(f'Вчера: {str_yesterday}')
print(f'Сегодня: {str_now}')
print(f'30 дней назад: {str_30_days_ago}')

some_date_str = '01/01/25 12:10:03.234567'
some_date = datetime.strptime(some_date_str, '%d/%m/%y %H:%M:%S.%f')
print('Некая дата', some_date)
