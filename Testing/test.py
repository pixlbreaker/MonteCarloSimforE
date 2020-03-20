import numpy as np
import math

sum = 0
y= []
def f(n):
    return (1/ math.factorial(n))

for i in range(0, 1000):
    y_i = f(i)
    y.append(y_i)


for i in range(0,len(y)):
    sum += y[i]

print(sum)

