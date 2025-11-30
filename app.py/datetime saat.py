import time
import datetime
import os


for a in range(10):
    print(datetime.datetime.now().strftime("%H:%M %S"))
    time.sleep(1)
    os.system('cls')