# import math
#
# print(math.sqrt(100))
import time
import datetime as d

print(d.datetime.now().year)


while True:
    time_now = time.localtime()
    print(f"{time_now.tm_hour}:{time_now.tm_min} {time_now.tm_sec}", end=" > ")
    time.sleep(1)





