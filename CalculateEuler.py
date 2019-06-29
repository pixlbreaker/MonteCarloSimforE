import numpy as np
import random

def SimulationSum():
    '''
    we take a random number from 0 to 1, then we take another one and add it to the first one and so on, while our sum is less than 1. ξ is a quantity of numbers taken. The mean value of ξ is the Euler's number, which is approximately 2,7182818284590452353602874713527…
    '''
    n = 0
    sum = 0
    while (sum  <= 1):
        sum += random.uniform(0,1)
        n += 1
    sumMean = np.mean(n)
    return sumMean 

def CalculateEuler(n):
    '''
    Number of times to run the check
    '''
    sumlist =[]
    for i in range(0, n):
        sumlist.append(SimulationSum())
    return np.mean(sumlist)