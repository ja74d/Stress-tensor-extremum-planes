import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = np.array([[2, 0, 0], [0, 3, 4], [0, 4, -3]])

Ia = a[0][0] + a[1][1] + a[2][2]

IIa = (a[0][0]*a[1][1])-(a[0][1]*a[1][0]) + (a[1][1]*a[2][2]) - (a[1][2]*a[2][1]) + (a[0][0]*a[2][2]) - (a[0][2]*a[2][0])

IIIa = np.linalg.det(a)
IIIa = round(IIIa, 2)

print("Ia:", Ia)
print("IIa:", IIa)
print("IIIa:", IIIa)

lmb = sp.symbols('lmb')

equation = -lmb**3 + Ia*lmb**2 - IIa*lmb + IIIa

solutions = sp.solve(equation, lmb)

#solutions= [round(sol, 3) for sol in solutions]

#print(solutions)

x1 = round(solutions[0], 3)
x2 = round(solutions[1], 3)
x3 = round(solutions[2], 3)


a1 = a - np.array([[x1, 0, 0], [0, x1, 0], [0, 0, x1]])

a2 = a - np.array([[x2, 0, 0], [0, x2, 0], [0, 0, x2]])

a3 = a - np.array([[x3, 0, 0], [0, x3, 0], [0, 0, x3]])

eigenvectors = np.linalg.eig(a)

eigenvectors = eigenvectors[1]

print(eigenvectors)

V1 = [eigenvectors[0][0], eigenvectors[1][0], eigenvectors[2][0]]
V2 = [eigenvectors[0][1], eigenvectors[1][1], eigenvectors[2][1]]
V3 = [eigenvectors[0][2], eigenvectors[1][2], eigenvectors[2][2]]

