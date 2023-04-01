import datetime

start_time = datetime.datetime.now()
print(start_time)

start_time = datetime.datetime(2016, 1, 11)
print(start_time)

end_time = start_time.replace(year=2017, month=2, day=1)
print(end_time)

how_long = end_time - start_time
print(how_long)
print(how_long.days)
print(how_long.seconds)

hundred_days = datetime.timedelta(days=100)
print(datetime.datetime.now() + hundred_days)
print(datetime.datetime.now() - hundred_days)
