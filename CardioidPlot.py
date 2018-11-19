#!/usr/bin/env python3

"""
Make polar cardioid 'flower' plots.
Short exercise in implementing a class in Python.
"""

import matplotlib.pyplot as plt
import numpy as np


class PolarFlower:
    """
    Generates a flower-like polar cardioid object.

    Attributes are the object name, its size, the number
    of 'petals' and the tilt, which is the angle of the object axis
    in radians relative to 0.

    The methods calculate theta and r values for plotting on a polar plot.
    """

    def __init__(self, name='StandardFlower', size=5, petals=5, tilt=0):
        self.name = name
        self.size = size
        self.petals = petals
        self.tilt = tilt

    def thetavals(self):
        return np.arange(0.0,2*np.pi,0.0075)

    def rvals(self):
        return (self.size / 2) + np.sin(self.petals*self.thetavals() + self.tilt)


# Choose how many instances to generate
num_flowers = 5

# Make a figure & axes
fig = plt.figure(num='PolarFlowers')
ax = fig.add_subplot(111,polar=True)

# Instantiate & plot the PolarFlower objects
for n in range(0,num_flowers):
    flower = PolarFlower( size=np.random.randint(1,10),
                            petals=np.random.randint(5,15),
                            tilt=np.pi / np.random.randint(1,12) )
    ax.plot(flower.thetavals(),flower.rvals(),linestyle='-')

# Remove tick labels & grid from plot
ax.set_xticks([])
ax.set_yticks([])
plt.grid(None)

# Set title & display plot
plt.title(str(num_flowers)+' random instances of the PolarFlower class')
plt.show()
