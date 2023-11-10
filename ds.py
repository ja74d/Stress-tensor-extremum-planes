import numpy as np

A = np.array([[2, 0, 0], [0, 3, 4], [0, 4, -3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

