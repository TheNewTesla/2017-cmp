
# coding: utf-8

# In[ ]:


#Lazar Novakovic Homework for confined Brownian motion.

get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import exp
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-10, 10)
ax.set_aspect(1)

x = [0]
y = [0]
line, = ax.plot(x, y, '-o', color='0.8', markerfacecolor='0', marker='.')

def update(frame, x, y):
    # Chooses a random direction
    d = np.random.random() * 2 * np.pi
    #Tried to constrict movement past boundries with logistic function.
    f = 1/(1+100*exp(-100*(d)))
    
    # Add steps, restricting movement between -10 and 10 for x and y

    
    if y[-1]<-10:
        x.append(x[-1] + np.cos(d))
        y.append(y[-1]+1) 
    elif y[-1]>10:
        x.append(x[-1] + np.cos(d))
        y.append(y[-1]-1)
    elif x[-1]<-10:
        x.append(x[-1] +1)
        y.append(y[-1]+ np.sin(d)) 
    elif x[-1]>10:
        x.append(x[-1] -1)
        y.append(y[-1] + np.sin(d)) 
    else:
        x.append(x[-1] + np.cos(d))
        y.append(y[-1] + np.sin(d)) 
    #This prevents too much clutter. Erases old values of motion.
    if len(x) > 200:
        x.pop(0)
        y.pop(0)



    # Updates the line.
    line.set_xdata(x)
    line.set_ydata(y)

    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))

    return line,

ani = animation.FuncAnimation(fig, update, fargs=(x, y), interval=10)
plt.show()

