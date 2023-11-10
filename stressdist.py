import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic 3D stress data
x = np.linspace(0, 10, 50)
y = np.linspace(0, 5, 25)
X, Y = np.meshgrid(x, y)
stress_data = 100 * np.sin(0.2 * X) + 50 * np.cos(0.2 * Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D surface plot of the stress data
surf = ax.plot_surface(X, Y, stress_data, cmap='viridis')

# Add color bar
fig.colorbar(surf)

# Set labels and title
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Stress')
ax.set_title('3D Stress Contour Plot')

plt.show()
