import numpy as np
import matplotlib.pyplot as plt
from utils.gaussian_plum_equations import Point, concentration_of_emission

initial_data = {
    "emission": 1,  # Example emission value (Q) [g/s]
    "height": 1,      # Example height of the stack (H) [m]
    "wind_speed": 5,   # Example wind speed (u) [m/s]
    "stability_class": "A"  # Example stability class (SC)
}

x_vals = np.arange(0.01, 101, 1)
y_vals = np.arange(-50, 51, 1)
z_val = 10  # Fixed z value (height)

X, Y = np.meshgrid(x_vals, y_vals)

concentration = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        point = Point(X[i, j], Y[i, j], z_val)
        concentration[i, j] = concentration_of_emission(initial_data, point)

# Plotting as a 2D heatmap
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, concentration, cmap='jet', levels=100)  # Contour plot for a smooth gradient
plt.colorbar(label=r'Concentration C [g/m$^3$]') 
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title(f"Concentration of emission at Z = {z_val}m")
plt.show()