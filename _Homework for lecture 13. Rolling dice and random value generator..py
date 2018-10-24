
# coding: utf-8

# In[ ]:





# In[55]:


#Lazar Novakovic
#Homework on dice rolls from Lecture 13
import numpy as np
import matplotlib.pyplot as plt

#Number of times we roll the dice
N = 333333
x = [0]
#I will do 3 separate runs for this calculation and then find the average.
for j in range(0,3):
    two6 = 0
    for i in range(N):
        #Random roll for dice a and b
        a = np.random.randint(1,7,1)
        b = np.random.randint(1,7,1)
        #Counts number of double 6 rolls.
        if a * b == 36:
            two6 += 1 
    #save number of rolled 6's
    x.append(two6)
    print("Run #", str(j+1),'Number of Double 6', two6)
    print('The probability of rolling a double six is', two6/N*100,"%")
k = sum(x) / float(3)

print("For",N, "rolls per run")
print("Theoretical value", 100/36,'%')
print("Average Probability over 3 runs", 100*k/N,'%')


# In[191]:


#Lazar Novakovic
#Random value generator of values between -5 and 5. Homework from lecture 13.

import numpy as np
import matplotlib.pyplot as plt

#These are the constants which will be used in the generation process of random values.
#This method is provided in the lecture pages.
N = 99
a = 545678
c = 1013904223
#I choose "relatively" prime values of 11 for c, 1013904223. Along with attempting random values of a I arrived with an even distribution.
m = 11
x = 1

#For storing values
values = []


for i in range(N):
    x = ((a*x+c)%m)
    values.append(x-5)
    
plt.plot(values,'o')
plt.show()

plt.hist(values)
plt.show()

print(values)
#For an unkown reason the histogram incorrectly displays the distribution of the values, 
#although counting the values in the array, there are not extra values of 5 generatied.

