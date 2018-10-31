
# coding: utf-8

# In[48]:


#New importance sampling for w(x)= x^-1
import matplotlib.pyplot as plt
import numpy as np
import random as random
from scipy.integrate import quad
from math import log

def h(x):
    return 1/(np.exp(x)+1)

def w(x):
    return 1/x
    # Given w(x) = x^-1

def IMontepython(N):
    I = 0
    A = quad(w,0,1)[0]
    for i in range(N):
        x = random.random()
        y = ((x**2) * (2*log((x))-1))/4
        I += h(y) 
        #Given by lecture 11
    I_n = (I * A) / N
        
    return I_n
print('Integral Value:', IMontepython(1000000))


# In[53]:


#This is the non-uniform distribution from Lecture #14



T = 3.053*60
t = np.linspace(0,1000,100)

y = (2**(-t/T)*np.log(2)/T)
Thal = []
Lead = []
NThal = 100
NLead = 0
N = 1000
N_time = 1000
N_Lead = np.zeros([N_time-1])  #the array to store the number of decayed atoms in each time step 
N_Thal = N * np.ones([N_time-1])

plt.plot(t,y)
plt.xlim(0,1000)
plt.show()


m = np.log(2)/T
x = []

for i in range(N):
    Thal.append(NThal)
    
    Lead.append(NLead)

    #Generating random value
    
    s = np.random.random()
    # Here is attempt at generating non-uniform distribution by forcing a gaussian-esque distribution of the decay.
    s_0 = (np.e**((-s**2)))
    x.append(-np.log(1-s)/m)
    x_0 = int(-np.log(1-s)/m)
    if x_0<N_time:   
        #Counting Decay
        N_Lead[x_0:] += 1 
        N_Thal[x_0:] -= 1 
        
plt.hist(x,100, density=1)
plt.xlim(0,1000)
plt.show()

plt.plot(N_Thal, label='Thalium')
plt.plot(N_Lead, label='Lead')
plt.xlabel("Time evolution")
plt.ylabel("Atoms")    
plt.legend()
plt.show()

