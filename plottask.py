#Weekly task 08

#author: Sofiia Meteliuk

#Write a program called plottask.py that displays:

#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range [0, 10], 
#on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc).



import matplotlib.pyplot as plt 
import numpy as np
from numpy import random

random.seed(123)

x = np.array(range(0,10))
y = x**3
plt.plot(x, y, 'r', label = "h(x)=x^3")


normdistr = random.normal(loc=5, scale = 2, size=1000)
plt.hist(normdistr, label='normal distribution')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Weekly task 08')
plt.legend(loc='upper left')
plt.grid( linestyle = '--', linewidth = 0.3)

plt.show() 