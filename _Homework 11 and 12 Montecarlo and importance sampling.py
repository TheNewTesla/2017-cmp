
# coding: utf-8

# In[31]:


#Lazar Novakovic
#Homework 11 and 12 Computational Physics 300

import matplotlib.pyplot as plt
import numpy as np
import random as random
from scipy.integrate import quad
from numba import jit
#Thanks to Daniel for @jit

#Intersection is at 1.6, therefore larger values are unnecessary.

@jit
def f1(x):
    return np.sqrt(1-(x-1)**2)
@jit
def f2(x):
    return 2-np.sqrt(4-x**2)

@jit
def Montepython(N):
    I = 0
    for i in range(N):
        x = 1.6*random.random()
        y = random.random()
        if y > f2(x) and y < f1(x):
            I += 1
    return 1.6*I/N
print('Integral Value:', Montepython(1000000))
@jit
def Montepython(N):
    I = 0
    for i in range(N):
        x = 1.6*random.random()
        y = random.random()
        if y > g(x) and y < f(x):
            I += 1
    return 1.6*I/N

@jit
def f(x):
    return np.sqrt(1-(x-1)**2)
@jit
def g(x):
    return 2-np.sqrt(4-x**2)

#The variance is standard deviation squared. sigma**2
@jit

def variation(N):
    var = 0
    p = Montepython(N)/1.6
    for i in range(100):
        var += (p*(1-p))/N
    average = var / 100
    return average

for i in range(2,6):
    print('Variance of N:', str(10**i), variation(10**i))
    
@jit
def h(x):
    return 1/(np.exp(x)+1)
@jit
def w(x):
    return 1/np.sqrt(x)
    # Given w(x) = x^-1/2
@jit
def IMontepython(N):
    I = 0
    A = quad(w,0,1)[0]
    for i in range(N):
        x = random.random()
        y = x**2
        I += h(y) 
        #Given by lecture 11
    I_n = (I * A) / N
        
    return I_n
print('Integral Value:', IMontepython(1000000))


# In[28]:





# In[29]:




