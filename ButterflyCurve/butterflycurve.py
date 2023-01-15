# importing the required module
import numpy as np
from math import *
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
 
theta = np.linspace( 0 , 12 * np.pi , 1000 ) 

    # x axis values
    # corresponding y axis values
x = np.sin(theta) * (np.exp(np.cos(theta))- (2 * np.cos(4*theta)) - (np.sin(theta/12))**5)
y = np.cos(theta) * (np.exp(np.cos(theta))- (2 * np.cos(4*theta)) - (np.sin(theta/12))**5)

# plotting the points
plt.plot(x, y)
plt.gca().set_aspect('equal') 

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title("Butterfly's curve")
 

# function to show the plot
plt.show()

#taken from the solution - coloured version of the buttefly's curve
from matplotlib import cm
from matplotlib.collections import LineCollection
r = np.sqrt(x**2 + y**2) # find the radius, then normalise.
r = r/max(r)
fig,ax = plt.subplots()
segments = []
for i in range(len(x)-1):
 segments.append([(x[i],y[i]),(x[i+1],y[i+1])])
coll = LineCollection(segments, cmap=plt.cm.rainbow,linewidth=0.8)
coll.set_array(r)
ax.add_collection(coll)
ax.set_aspect('equal')
ax.autoscale_view()
ax.axis('off')
plt.show()
