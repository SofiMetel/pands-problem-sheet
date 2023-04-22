#Weekly task 08

#author: Sofiia Meteliuk
'''
Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).
'''
#I used tutorials from https://www.w3schools.com/python/matplotlib_pyplot.asp 

import matplotlib.pyplot as plt #import matplotlib
import numpy as np #import numpy 
from numpy import random #import random from numpy for simplyfying reading code

random.seed(123)

x = np.array(range(0,10))
y = x**3
plt.plot(x, y, 'r', label = "h(x)=x^3")


normdistr = random.normal(loc=5, scale = 2, size=1000) #a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
plt.hist(normdistr, label='normal distribution') #creating histogram of normal distribution

plt.xlabel('x') #adding label to x-axes
plt.ylabel('y') #adding label to y-axes
plt.title('Weekly task 08') #setting title of plot
plt.legend(loc='upper left') #determine position of legend notation
plt.grid( linestyle = '--', linewidth = 0.3) #making grid less visible 

plt.show() 