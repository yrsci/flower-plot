#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Make a cardioid plot. Small exercise in using classes in Python.
"""

import matplotlib.pyplot as plt
import numpy as np


class PolarFlower:

    def __init__(self, name="StandardFlower", size=5, petals=5, tilt=0):
        self.name = str(name)
        self.size = size
        self.petals = petals
        self.tilt = tilt

    def thetavals(self):
        return np.arange(0.0,2*np.pi,0.025)

    def rvals(self):
        return (self.size / 2) + np.sin(self.petals*self.thetavals() + self.tilt)

# Make an object:
standard_flower = PolarFlower()

# Plot the object
fig = plt.figure()
plt.polar(standard_flower.thetavals(),standard_flower.rvals(),
            label=standard_flower.name,linestyle='-')
plt.legend()
plt.show()
