import statistics
import random
import time


def generate_num():
    """
    Generates a number from 0 to 1
    """
    x = random.uniform(0,1)
    return x

def calculate_sum(sum, x):
    """
    Calculates the sum of the values in the list
    """
    return sum + x
    # sum = 0
    # for i in range(len(lst)):
    #     sum += lst[i]
    # return sum

# count = 0
# sum = 0
# values = []
# while True:
#     x = generate_num()
#     if calculate_sum(sum, x) < 1:
        




def SimulationSum():
    '''
    we take a random number from 0 to 1, then we take another one and add it to the first one and so on, while our sum is less than 1. ξ is a quantity of numbers taken. The mean value of ξ is the Euler's number, which is approximately 2,7182818284590452353602874713527…
    '''
    sum = 0
    count = 0
    while sum < 1:
        x = random.uniform(0,1)
        sum += x
        count += 1
    return count

def CalculateEuler(n):
    '''
    Number of times to run the check
    '''
    sumlist =[]
    for i in range(0, n):
        sumlist.append(SimulationSum())
    return np.mean(sumlist)