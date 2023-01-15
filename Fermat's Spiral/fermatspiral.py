# importing the required module
import numpy as np
from math import *
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
 
theta = np.linspace( 0 , 10 * np.pi , 1000 ) 

    # x axis values
    # corresponding y axis values
x = (theta ** 0.5 )* np.cos(theta)
y = (theta ** 0.5 )* np.sin(theta) 


# plotting the points
plt.plot(x, y, color = "blue")

x = -(theta ** 0.5 ) * np.cos(theta)
y = -(theta ** 0.5 ) * np.sin(theta)

plt.plot(x, y, color = "blue")
 
plt.gca().set_aspect('equal') 

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title("Fermat's Spiral")
 

# function to show the plot
plt.show()
