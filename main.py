# Matplotlib imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# Calculate Euler import
import CalculateEuler

# Time imports
import time

while True:
    value = CalculateEuler.CalculateEuler(10)
    print(value)
    time.sleep(50/1000)


# Change the style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xs =[]
    ys =[]

    for i in range(0, 1000):
        value = CalculateEuler.CalculateEuler(i)
        xs.append(i+1)
        ys.append(value)
        ax1.clear()
        ax1.plot(xs, ys)
        print("On run {0} the value is: {1}".format(i, value))


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()

