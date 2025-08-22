#Finding Steady States 
# Importing Libraries
import matplotlib.pyplot as plt
from sympy import symbols, solve

# Defining Steady States
SS1x = []
SS1s = []
SS2x = []
SS2s = []

# Defining Parameters
Alpha_values = [1.01, 1.1, 1.5, 2.0]  # Test different values for Alpha
Gamma = 0.5
Y = 0.5

s, x = symbols('s, x', real=True)

for Alpha_value in Alpha_values:
    Roots = solve(Alpha_value * ((s * x) / (Gamma + s)) - x, [s, x])
    sSS1 = Roots[0][0]
    xSS2 = Roots[1][1]
    xSS1 = solve(1 - sSS1 - (Alpha_value / Y) * ((sSS1 * x) / (Gamma + sSS1)), [x])[0]
    sSS2 = solve(1 - s - (Alpha_value / Y) * ((s * xSS2) / (Gamma + s)), [s])[0]

    SS1x.append(xSS1)
    SS1s.append(sSS1)
    SS2x.append(xSS2)
    SS2s.append(sSS2)

# Plotting
plt.figure()
plt.plot(Alpha_values, SS1x, label='SteadyState 1 X')
plt.plot(Alpha_values, SS2x, label='SteadyState 2 X')
plt.legend()
plt.xlabel('Alpha')
plt.ylabel('Steady State X')
plt.title('Steady State X vs Alpha')

plt.figure()
plt.plot(Alpha_values, SS1s, label='SteadyState 1 S')
plt.plot(Alpha_values, SS2s, label='SteadyState 2 S')
plt.legend()
plt.xlabel('Alpha')
plt.ylabel('Steady State S')
plt.title('Steady State S vs Alpha')

plt.show()
