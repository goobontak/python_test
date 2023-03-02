import datetime
import time
current_time = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
new_time = current_time + datetime.timedelta(minutes=65)
new_time_int = new_time.strftime("%H : %M : %S")
print(new_time_int)