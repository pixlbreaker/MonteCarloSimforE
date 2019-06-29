import random
import math

count_inside = 0
for count in range(0, 100000):
    d = math.hypot(random.random(), random.random())
    print('d :' + str(d))
    if d < 1: count_inside += 1
count += 1
print( 4.0 * count_inside / count)
