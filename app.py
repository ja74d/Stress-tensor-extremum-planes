import numpy as np

a = np.array([[2, 0, 0], [0, 3, 4], [0, 4, -3]])

Ia = a[0][0] + a[1][1] + a[2][2]

IIa = (a[0][0]*a[1][1])-(a[0][1]*a[1][0]) + (a[1][1]*a[2][2]) - (a[1][2]*a[2][1]) + (a[0][0]*a[2][2]) - (a[0][2]*a[2][0])

IIIa = np.linalg.det(a)
IIIa = round(IIIa, 2)

