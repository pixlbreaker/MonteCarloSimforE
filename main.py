# Matplotlib imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# Calculate Euler import
import CalculateEuler

# import threading
import threading
import time

import statistics
import random

e_lst = []

def animation_graph():
    print("This is outside the thread")

def SimulationSum():
    '''
    we take a random number from 0 to 1, then we take another one and add it to the first one and so on, while our sum is less than 1. ξ is a quantity of numbers taken. The mean value of ξ is the Euler's number, which is approximately 2,7182818284590452353602874713527…
    '''
    sum = 0
    count = 0
    while sum < 1:

        # Random value between 0 and 1
        x = random.uniform(0,1)
        sum += x
        count += 1
    return count

def CalculateEuler(n):
    '''
    Runs the simulation function constantly to get the value of e
    '''
    sumlist = []
    e = 0
    while len(sumlist) != n:
        sumlist.append(SimulationSum())
        e = statistics.mean(sumlist)
        e_lst.append(e)
        print("On run " + str(len(sumlist)) + " e is " + str(e))
        # Sleeps for 50 ms
        time.sleep(50/1000)
    return e


cal = CalculateEuler
# e = cal.CalculateEuler(1000)

calculation_thread= threading.Thread(target = CalculateEuler(10), args = ())
calculation_thread.setDaemon(True)
calculation_thread.start()

animation_thread = threading.Thread(target=animation_graph(), args=())
animation_thread.start()

calculation_thread.join()
animation_thread.join()




# print("The final value of e is " + str(e))
#print("This is outside the thread")
print(len(cal.e_lst))


