import numpy as np
import matplotlib.pyplot as plt
from utils.gaussian_plum_equations import Point, concentration_of_emission

# Define the initial data (example values)
initial_data = {
    "emission": 1000,  # Example emission value (Q)
    "height": 50,      # Example height of the stack (H)
    "wind_speed": 5,   # Example wind speed (u)
    "stability_class": "A"  # Example stability class (SC)
}

# Generate grid of x, y values for the slice at z = 60
x_vals = np.arange(0.01, 101, 1)  # x from 0 to 100
y_vals = np.arange(-50, 51, 1)  # y from -50 to 50
z_val = 60  # Fixed z value (height)

# Create meshgrid for x, y
X, Y = np.meshgrid(x_vals, y_vals)

# Compute concentrations for each (x, y, z=60) point
concentration = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        point = Point(X[i, j], Y[i, j], z_val)
        concentration[i, j] = concentration_of_emission(initial_data, point)

# Plotting as a 2D heatmap
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, concentration, cmap='jet', levels=100)  # Contour plot for a smooth gradient
plt.colorbar(label='Concentration')  # Color bar to show concentration levels
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f"Concentration of Emission at Z = {z_val}")
plt.show()