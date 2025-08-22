#Vapor Pressures & Activity Coefficients for Acetone,Chloroform, Methanol
import numpy as np

# molar volume interpolation
#temperature and molar volume data (t in K)
T_acetone = np.array([228.15, 272.15, 323.15])  
V_acetone = np.array([67.380, 71.483, 76.826])  # in cc/g mol

T_chloroform = np.array([273.15, 303.15, 333.15])  
V_chloroform = np.array([78.218, 81.185, 84.5])  

T_methanol = np.array([273.15, 373.15, 473.15])  
V_methanol = np.array([39.556, 44.874, 57.939])  

# temperature we want: 57.5°C = 330.65K
T_target = 330.65

# interpolation for molar volumes at 330.65K
V_acetone_interp = np.interp(T_target, T_acetone, V_acetone)
V_chloroform_interp = np.interp(T_target, T_chloroform, V_chloroform)
V_methanol_interp = np.interp(T_target, T_methanol, V_methanol)

print(f"Interpolated molar volume of Acetone: {V_acetone_interp:.4f} cc/g mol")
print(f"Interpolated molar volume of Chloroform: {V_chloroform_interp:.4f} cc/g mol")
print(f"Interpolated molar volume of Methanol: {V_methanol_interp:.4f} cc/g mol")

#wilson and antiones
# Given data for mole fractions
x_acetone = 0.30
x_chloroform = 0.47
x_methanol = 0.23

#  wilson (from gamma12 - gamma11 and gamma12 - gamma22)
Lambda_acetone_chloroform = np.exp(-72.20 / (8.314 * 57.5))  # Acetone/Chloroform
Lambda_chloroform_acetone = np.exp(-332.23 / (8.314 * 57.5))
Lambda_acetone_methanol = np.exp(-214.95 / (8.314 * 57.5))  # Acetone/Methanol
Lambda_methanol_acetone = np.exp(664.08 / (8.314 * 57.5))
Lambda_chloroform_methanol = np.exp(-373.30 / (8.314 * 57.5))  # Chloroform/Methanol
Lambda_methanol_chloroform = np.exp(1703.68 / (8.314 * 57.5))

# antione constants
# acetone values
A_acetone = 7.02447
B_acetone = 1161.0
C_acetone = 224.0

# chloroform values
A_chloroform = 6.90328
B_chloroform = 1163.03
C_chloroform = 227.4

# methanol values
A_methanol = 7.87863
B_methanol = 1473.11
C_methanol = 230.0

# antiones at 57.7 (C)
def antoine_eq(A, B, C, T):
    return 10 ** (A - (B / (T + C)))
T = 57.5
# calculate vp and convert to atm
P_acetone_0 = antoine_eq(A_acetone, B_acetone, C_acetone, T) / 760
P_chloroform_0 = antoine_eq(A_chloroform, B_chloroform, C_chloroform, T) / 760
P_methanol_0 = antoine_eq(A_methanol, B_methanol, C_methanol, T) / 760

# Wilson equations
def gamma_wilson(x1, x2, Lambda12, Lambda21):
    return np.exp(-np.log(x1 * Lambda12 + x2 * Lambda21) + 1 - (x2 * Lambda21 / (x1 * Lambda12 + x2 * Lambda21)))

# AC for each 
gamma_acetone = gamma_wilson(x_acetone, x_chloroform, Lambda_acetone_chloroform, Lambda_chloroform_acetone)
gamma_chloroform = gamma_wilson(x_chloroform, x_acetone, Lambda_chloroform_acetone, Lambda_acetone_chloroform)
gamma_methanol = gamma_wilson(x_methanol, x_acetone, Lambda_methanol_acetone, Lambda_acetone_methanol)

#chloro/methanol
gamma_chloroform_methanol = gamma_wilson(x_chloroform, x_methanol, Lambda_chloroform_methanol, Lambda_methanol_chloroform)
gamma_methanol_chloroform = gamma_wilson(x_methanol, x_chloroform, Lambda_methanol_chloroform, Lambda_chloroform_methanol)

# total pressure via raoults
P_total = (x_acetone * gamma_acetone * P_acetone_0 +
           x_chloroform * gamma_chloroform * P_chloroform_0 +
           x_methanol * gamma_methanol * P_methanol_0)

P_experimental = 1.0  # atm

# percent errror calcs
percent_error = abs(1.0-P_total)/P_total* 100

# Output the results
print(f"Vapor pressure of Acetone: {P_acetone_0:.4f} atm")
print(f"Vapor pressure of Chloroform: {P_chloroform_0:.4f} atm")
print(f"Vapor pressure of Methanol: {P_methanol_0:.4f} atm")

print(f"Activity coefficient of Acetone: {gamma_acetone:.4f}")
print(f"Activity coefficient of Chloroform: {gamma_chloroform:.4f}")
print(f"Activity coefficient of Methanol: {gamma_methanol:.4f}")

print(f"Total pressure: {P_total:.4f} atm")
print(f"Percentage error: {percent_error:.2f} %")
