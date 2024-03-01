import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd


class Material:
    def __init__(self, ro, lambd, c_p, mu=None, beta=None):
        self.ro = ro
        self.lambd = lambd
        self.c_p = c_p
        self.mu = mu
        self.beta = beta


water = Material(997, 0.6069, 4187.7, mu=0.0008899, beta=0.000257)
wood = Material(510, 0.12, 1380)
iron = Material(7870, 80.2, 447)

g = 9.8066502
L = H = 0.01
L_solid = 0.4 * L
wood_T = 325.22
iron_T = 274.78
delta_T = 279.527 - 274.849

Gr = (g * water.beta * delta_T * L ** 3) / ((water.mu / water.ro) ** 2)
Pr = water.mu * water.c_p / water.lambd
Pa = Gr * Pr
Nu_av = 0.18 * ((Gr * (Pr ** 2)) / (0.2 + Pr)) ** 0.29
print(Gr, Pr, Pa, Nu_av)

v_b = sqrt(g * water.beta * delta_T * H)
t_conv = H / v_b
print(v_b, t_conv)
t_heat_wood = (wood.ro * water.c_p * L_solid ** 2) / wood.lambd
t_heat_iron = (iron.ro * iron.c_p * L_solid ** 2) / iron.lambd
print(t_heat_wood, t_heat_iron)

q = (wood_T - iron_T) / (L_solid / wood.lambd + L_solid / iron.lambd + L / ((0.18 * Pa ** 0.25) * water.lambd))
print(q)
T_left = wood_T - q * L_solid / wood.lambd
T_right = iron_T + q * L_solid / iron.lambd
print(T_left, T_right, T_left - T_right)

data_1 = pd.read_csv('1.csv', skiprows=5, usecols=[1, 3])
data_2 = pd.read_csv('2.csv', skiprows=5, usecols=[1, 3])

plt.scatter(data_1.iloc[:, 1], data_1.iloc[:, 0], label='Левая стенка')
plt.scatter(np.abs(data_2.iloc[:, 1].to_numpy()), data_2.iloc[:, 0], label='Правая стенка')
plt.ylabel('y, м')
plt.xlabel('Nu')
plt.grid(True)
plt.legend()
plt.show()
