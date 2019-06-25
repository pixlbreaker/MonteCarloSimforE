import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

import CalculateEuler

# x = np.arange(0.0, 3.0, 0.001)
# y = x

# fig, ax = plt.subplots()
# ax.plot(x,y)
# ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig('test.png')
# plt.show()


list = []
for i in range(0, 1000):
    value = CalculateEuler.CalculateEuler(i)
    list.append(value)
    print("On run {0} the value is: {1}".format(i, value))
plt.plot(list)
plt.show()
#CalculateEuler.CalculateETest()