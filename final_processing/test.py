import datetime

current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")

current_time = datetime.datetime.strptime(current_time, "%H:%M:%S.%f")
print(current_time)
