#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Temperature Drops at Different Radii

import numpy as np
import matplotlib.pyplot as plt

# givens
T_surr = -10 # C
T_fluid = 50 # C
k_ss = 16 # W/m K
# wall thickness of ss is 1/16 inches
d_walls = 0.0016 # meters
# thickness of the vacuum gap = 1 mm
d_vac = 0.0010 # meters
# assumption that the cylinder radius is 1.5 inches
r1 = 0.0381 # meters
H = 0.3162 # height of flask

# the radius values
r2 = r1 + d_walls
r3 = r2 + d_vac
r4 = r3 + d_walls

# radius values and temperatures (zeros)
r_vals = np.linspace(0,r4,200)
Temp = np.zeros_like(r_vals)

# temperature plot of the fluid (assumption: constant)
A = (r_vals >= 0) & (r_vals < r1)
Temp[A] = T_fluid

# get Q and R of the inner walls
R_in = np.log(r2/r1)/(2*np.pi*k_ss*H)
q = (T_fluid - T_surr)/(R_in)/2

#temperature drop plot
B = (r_vals >= r1) & (r_vals < r2)
Temp[B] = T_fluid - (q*R_in/d_walls)*(r_vals[B] - r1)

# temperature in vacuum
C = (r_vals >= r2) & (r_vals < r3)
Temp[C] = Temp[B][-1]

# Q and R for outer wall
R_out = np.log(r4/r3)/(2*np.pi*k_ss*H)
q2 = (T_fluid - T_surr)/(R_out)/2

# temperature drop outerwall
D = (r_vals >= r3) & (r_vals < r4)
Temp[D] = Temp[B][-1] - (q2*R_out/d_walls)*(r_vals[D] - r3)

# temp  outer wall
Temp[-1] = -10

# a graph the profile
plt.subplot(1,2,1)
plt.plot(r_vals, Temp, 'b-')
plt.xlabel("Radius (Meters)")
plt.ylabel("Temperature (Celsius)")

plt.subplot(1,2,2)
plt.plot(r_vals[-30:],Temp[-30:])
plt.title("Zoomed in on relevant radii")
plt.axvline(x=r1, color='red', label="r1",)
plt.axvline(x=r2, color='orange', label="r2")
plt.axvline(x=r3, color='pink', label="r3")
plt.xlabel("Radius (Meters)")
plt.legend()
plt.show()
