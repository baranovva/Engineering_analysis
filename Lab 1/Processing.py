import numpy as np
from scipy.linalg import solve
from math import sqrt


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

v_b = sqrt(g * water.beta * delta_T * H ** 3)
t_conv = H / v_b
print(v_b, t_conv)
t_heat_wood = (wood.ro * water.c_p * L_solid ** 2) / wood.lambd
t_heat_iron = (iron.ro * iron.c_p * L_solid ** 2) / wood.lambd
print(t_heat_wood, t_heat_iron)

a = Nu_av * water.lambd / L

A = np.array([[1, wood.lambd / L_solid, 0, 0, 0],
              [1, -a, a, 0, 0],
              [1, 0, -water.lambd / L, water.lambd / L, 0],
              [1, 0, 0, -a, a],
              [1, 0, 0, 0, -iron.lambd / L_solid]])

b = np.array([wood.lambd * wood_T / L_solid, 0, 0, 0, - iron.lambd * iron_T / L_solid])
x = solve(A, b)
print(x)
print(x[2] - x[3], delta_T)
