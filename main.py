import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0.0, 3.0, 0.001)
y = x

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
ax.grid()

fig.savefig('test.png')
plt.show()


print("Hello World")