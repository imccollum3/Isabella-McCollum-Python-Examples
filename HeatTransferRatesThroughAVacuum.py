#Heat Transfer Rates Through a Vacuum
import numpy as np
import matplotlib.pyplot as plt

# givens
T_surr = -10 # C
T_fluid = 50 # C
k_ss = 16 # W/m K
k_air = 0.0143
# wall thickness of ss is 1/16 inches
d_walls = 0.0016 # meters
# thickness of the vacuum gap = 1 mm
d_vac = 0.0010 # meters
r1 = 0.0005 # meters  (random value that makes graph look nice)
H = 0.3162 # height of flask

# new rad values
r2 = r1 + d_walls
r3 = r2 + d_vac
r4 = r3 + d_walls

# resistances of all walls and the air gap
R_in = np.log(r2/r1)/(2*np.pi*k_ss*H)
R_gap = np.log(r3/r2)/(2*np.pi*k_air*H)
R_out = np.log(r4/r3)/(2*np.pi*k_ss*H)
R_tot = R_in + R_gap + R_out
q = (T_fluid - T_surr)/R_tot # watts

# temperature drop (ΔT = q*R)
Tdrop1 = q*R_in
Tdrop2 = q*R_gap
Tdrop3 = q*R_out

# radii 
r_vals = np.array([0,r1,r2,r3,r4])

#temperature at each radii
T_r1 = T_fluid
T_r2 = T_fluid - Tdrop1
T_r3 = T_fluid - Tdrop1 - Tdrop2
T_r4 = T_surr
Temps = np.array([T_fluid, T_r1, T_r2, T_r3, T_r4])

# plot of the temperature profiel
plt.plot(r_vals, Temps, 'b.-')
plt.xlabel("Radius (Meters)")
plt.ylabel("Temperature (Celsius)")
plt.axvline(x=r1, color='red',label='r1')
plt.axvline(x=r2, color='orange',label='r2')
plt.axvline(x=r3, color='green',label='r3')
plt.axvline(x=r4, color='pink',label='r4')
plt.legend()
