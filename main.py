# Imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import threading
import multiprocessing
import time
import random

# Calculate Euler import
import CalculateEuler

x_vals = []
y_vals = []

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))

if __name__ == "__main__":

    cal = CalculateEuler

    # animation_thread = multiprocessing.Process(target=animation_function(), args=())
    # animation_thread.daemon = True
    # animation_thread.start()

    #plt.show()

    calculation_thread = multiprocessing.Process(target = cal.CalculateEuler(), args = ())
    calculation_thread.daemon = True
    calculation_thread.start()

    calculation_thread.join()
    #animation_thread.join()

    print(len(cal.e_lst))


