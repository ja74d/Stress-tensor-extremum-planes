import numpy as np
import sympy as sp

a = np.array([[2, 0, 0], [0, 3, 4], [0, 4, -3]])

Ia = a[0][0] + a[1][1] + a[2][2]

IIa = (a[0][0]*a[1][1])-(a[0][1]*a[1][0]) + (a[1][1]*a[2][2]) - (a[1][2]*a[2][1]) + (a[0][0]*a[2][2]) - (a[0][2]*a[2][0])

IIIa = np.linalg.det(a)
IIIa = round(IIIa, 2)

lmb = sp.symbols('lmb')

equation = -lmb**3 + Ia*lmb**2 - IIa*lmb + IIIa

solutions = sp.solve(equation, lmb)

solutions= [round(sol) for sol in solutions]

a1 = a - np.array([[solutions[0], 0, 0], [0, solutions[0], 0], [0, 0, solutions[0]]])

a2 = a - np.array([[solutions[1], 0, 0], [0, solutions[1], 0], [0, 0, solutions[1]]])

a3 = a - np.array([[solutions[2], 0, 0], [0, solutions[2], 0], [0, 0, solutions[2]]])

