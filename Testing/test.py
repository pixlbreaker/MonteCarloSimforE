import numpy as np
import statistics
import math
import random
import time


def SimSum():
    sum = 0
    count = 0
    while sum < 1:
        x = random.uniform(0,1)
        sum += x
        count += 1
    #print(count)
    return count


lst = []
while True:
    lst.append(SimSum())
    e = statistics.mean(lst)
    print("On run " + str(len(lst)) + " e is " + str(e))
    time.sleep(50/1000)
# sum = 0
# while True:
#     val = SimSum()
#     lst.append(val)

#     sum += val

#     e = sum / (len(lst))
#     #print(e)
#     time.sleep(50/1000)


