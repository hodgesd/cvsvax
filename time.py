import datetime

asof = "2021-02-20T10:55:42.098"
#date_time_str = '2018-06-29 08:15:27.243860'
date_time_str = asof
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)
