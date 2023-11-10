import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#Input Tensor
a = np.array([[2, 1, 7], [0, 3, 4], [0, 4, -3]])

#Invariants
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


#Results of Equation
x1 = round(solutions[0], 3)
x2 = round(solutions[1], 3)
x3 = round(solutions[2], 3)

#Tensor - Lambda
a1 = a - np.array([[x1, 0, 0], [0, x1, 0], [0, 0, x1]])

a2 = a - np.array([[x2, 0, 0], [0, x2, 0], [0, 0, x2]])

a3 = a - np.array([[x3, 0, 0], [0, x3, 0], [0, 0, x3]])

eigenvectors = np.linalg.eig(a)

eigenvectors = eigenvectors[1]

print(eigenvectors)

#eigenvectors

v1 = [eigenvectors[0][0], eigenvectors[1][0], eigenvectors[2][0]]
v2 = [eigenvectors[0][1], eigenvectors[1][1], eigenvectors[2][1]]
v3 = [eigenvectors[0][2], eigenvectors[1][2], eigenvectors[2][2]]

#Plot
# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each vector with a different color
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='Vector 1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', label='Vector 2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='Vector 3')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits
ax.set_xlim([0, max(v1[0], v2[0], v3[0])])
ax.set_ylim([0, max(v1[1], v2[1], v3[1])])
ax.set_zlim([0, max(v1[2], v2[2], v3[2])])

# Set aspect ratio
ax.set_box_aspect([max(v1[0], v2[0], v3[0]), max(v1[1], v2[1], v3[1]), max(v1[2], v2[2], v3[2])])

# Add a legend
ax.legend()

# Show the plot
plt.show()
