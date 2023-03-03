import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a 3D plot
fig = plt.figure()
fig.suptitle('Excavator 3D-Spatial System', fontsize=16)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Define the coordinates of the points
x_points = [0, 5]
y_points = [0, 0]
z_points = [0, 5]

# Plot the points
ax.scatter(x_points, y_points, z_points, color='red')

# Define the coordinates of the line
x = np.linspace(-10, 10, 100)
y = np.zeros_like(x)
z = np.ones_like(x) * -5

# Define the coordinates of the plane
X, Y = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))
Z = np.zeros_like(X)

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5)

# Plot the line
ax.plot(x, y, z, color='blue')

# Set the axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Show the plot
plt.show()