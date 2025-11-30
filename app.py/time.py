import time
import datetime


print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%H:%M %S"))


for a in range(10):
    print(datetime.datetime.now().strftime("%H:%M %S"))
    time.sleep(1)
