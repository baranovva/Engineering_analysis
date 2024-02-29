import numpy as np
import matplotlib.pyplot as plt
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
Nu_av = 0.18 * ((Gr * (Pr ** 2)) / (0.2 + Pr)) ** 0.29
print(Gr, Pr, Gr * Pr, Nu_av)

v_b = sqrt(g * water.beta * delta_T * H ** 3)
t_conv = H / v_b
print(v_b, t_conv)
t_heat_wood = (wood.ro * water.c_p * L_solid ** 2) / wood.lambd
t_heat_iron = (iron.ro * iron.c_p * L_solid ** 2) / wood.lambd
print(t_heat_wood, t_heat_iron)

q = (wood_T - iron_T) / (L_solid / wood.lambd + L_solid / iron.lambd + L / ((0.18 * (Gr * Pr) ** 0.25) * water.lambd))
print(q)
T_left = wood_T - q * L_solid / wood.lambd
T_right = iron_T + q * L_solid / iron.lambd
print(T_left, T_right, T_left - T_right)

y = np.array([0, 3.33E-4, 6.67E-4, 1E-3, 1.33E-3, 1.67E-3,
              2E-3, 2.33E-3, 2.67E-3, 3E-3, 3.33E-3, 3.67E-3,
              4E-3, 4.33E-3, 4.67E-3, 5E-3, 5.33E-3, 5.67E-3,
              6E-3, 6.33E-3, 6.67E-3, 7E-3, 7.33E-3, 7.67E-3,
              8E-3, 8.33E-3, 8.67E-3, 9E-3, 9.33E-3, 9.67E-3,
              1E-2])

Nu_left = np.array([2.47, 4.97, 4.99, 5, 5, 4.99,
                    4.98, 4.98, 4.97, 4.97, 4.94, 4.92,
                    4.92, 4.91, 4.91, 4.91, 4.9, 4.9,
                    4.9, 4.9, 4.89, 4.85, 4.84, 4.83,
                    4.83, 4.73, 4.59, 4.45, 4.26, 4.16,
                    2.06])

Nu_right = np.abs(np.array([0, -6.49E-01, -7.44E-01, -9.2E-01, -1.17, -1.47,
                            -1.8, -2.13, -2.45, -2.77, -3.08, -3.39,
                            -3.69, -3.99, -4.3, -4.62, -4.94, -5.28,
                            -5.63, -6.01, -6.39, -6.8, -7.22, -7.66,
                            -8.11, -8.54, -8.92, -9.21, -9.3, - 9.09,
                            0]))

plt.scatter(Nu_left, y, label='Левая стенка')
plt.scatter(Nu_right, y, label='Правая стенка')
plt.ylabel('y, м')
plt.xlabel('Nu')
plt.grid(True)
plt.legend()
plt.show()
