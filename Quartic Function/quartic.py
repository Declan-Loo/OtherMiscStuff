# importing the required module
import numpy as np
from math import *
import matplotlib.pyplot as plt
 
x = np.linspace(-3.3,2,1000)
print(x)
y = []
for lol in x:
    count = float(lol)
    
    #Formula: (x+2)(x-1)(x+3) - the graph should have 3 points of intersection with the x-axis, (0,0), (1,0) and (-3,0)
    y.append((count**2) * (count-1) * (count+3))
plt.plot(x, y)

x = [-4,2.1]
y = [0,0]

plt.plot(x,y)


# plotting the points
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title("Quartic Formula")
 

# function to show the plot
plt.show()
