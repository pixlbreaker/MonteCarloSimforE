import statistics
import random
import time


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
        print("On run " + str(len(sumlist)) + " e is " + str(e))
        # Sleeps for 50 ms
        time.sleep(50/1000)
    return e
