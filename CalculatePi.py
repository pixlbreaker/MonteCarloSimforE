import math
import random
import numpy
import time

points = []

def generate_point():
    """
    Generates a point in the first quadrant
    """

    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    point = (x,y)
    points.append(point)
    return point

def calculate_length(point):
    """
    Calculates the length of the point to the origin
    """
    val = math.pow(point[0], 2) + math.pow(point[1], 2)
    d = math.sqrt(val)
    return d

n = 0
count = 0
while True:
    n += 1
    pt = generate_point()
    d = calculate_length(pt)
    if d < 1:
        count += 1
    cal_pi = 4 * (count / n)
    print("n : %2d with a calculated pi value of %2.5f"%(n, cal_pi))
    time.sleep(10/1000)
