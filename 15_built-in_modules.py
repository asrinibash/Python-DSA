# how to use them

import math # first import it
import random
import time
import os

math.pi # now using math object we can access the its functions

random.randint(1,10)

a=[1,2,3,4,5]
random.shuffle(a) # it will shuffle the indexes
print(a)

print(time.time())  # current time
print(time.ctime())  # current time according to current location - Sat Aug 16 04:37:45 2025
time.sleep(1) # delay 1 second


print(os.getcwd()) # for get current working directory
print(os.listdir()) #like ls command