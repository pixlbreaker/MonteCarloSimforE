# Imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import threading
import multiprocessing
import time

# Calculate Euler import
import CalculateEuler

# Creates the figure
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
cal = CalculateEuler

# Creates the subplot
# def animation_graph():
#     xs = []
#     ys = []
#     count = 0
#     while count != len(cal.e_lst):
#         xs.append(float(count))
#         ys.append(cal.e_lst[count])
#         ax1.clear()
        

#         plt.xlabel('Date')
#         plt.ylabel('Price')
#         plt.title('Live graph with matplotlib')

#         count += 1
#         time.sleep(50/100)
	
#     ax1.plot(xs, ys)
    
def animation_thread_function():
    print("Hello")
    #ani = animation.FuncAnimation(fig, animation_graph, interval=1000) 


if __name__ == "__main__":

    calculation_thread = multiprocessing.Process(target = cal.CalculateEuler(), args = ())
    calculation_thread.daemon = True
    calculation_thread.start()

    animation_thread = multiprocessing.Process(target=animation_thread_function(), args=())
    animation_thread.daemon = True
    animation_thread.start()



    calculation_thread.join()
    animation_thread.join()



    # plt.show()

    # print("The final value of e is " + str(e))
    #print("This is outside the thread")
    print(len(cal.e_lst))


