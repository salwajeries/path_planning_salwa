
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Function to calculate curvature
def calculate_curvature(x, y):
    dx = np.gradient(x)
    dy = np.gradient(y)
    ddx = np.gradient(dx)
    ddy = np.gradient(dy)
    curvature = np.abs(dx * ddy - dy * ddx) / (dx**2 + dy**2)**1.5
    return curvature

# Load the CSV file
data = pd.read_csv('BrandsHatchLayout.csv')
data_cleaned = data.dropna()

# Extract x, y coordinates for left and right cones
left_cones = data_cleaned[data_cleaned['side'] == 'left']
right_cones = data_cleaned[data_cleaned['side'] == 'right']

x_left = left_cones['x'].values
y_left = left_cones['y'].values

x_right = right_cones['x'].values
y_right = right_cones['y'].values

# Create a centerline by averaging left and right cone positions
x_center = (x_left + x_right) / 2
y_center = (y_left + y_right) / 2

# Sort the centerline data by x values
centerline_data = pd.DataFrame({'x': x_center, 'y': y_center})
centerline_data = centerline_data.sort_values(by='x')

# Extract sorted x and y values
x_center_sorted = centerline_data['x'].values
y_center_sorted = centerline_data['y'].values

# Interpolate the centerline using cubic splines
centerline_spline = CubicSpline(x_center_sorted, y_center_sorted)
x_smooth = np.linspace(x_center_sorted.min(), x_center_sorted.max(), 500)
y_smooth = centerline_spline(x_smooth)

# Calculate curvature
curvature = calculate_curvature(x_smooth, y_smooth)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(x_left, y_left, 'bo', label='Left Cones')
plt.plot(x_right, y_right, 'ro', label='Right Cones')
plt.plot(x_smooth, y_smooth, 'g-', linewidth=2, label='Centerline (Smoothed)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Path Planning with Smoothed Centerline')
plt.legend()
plt.grid(True)
plt.savefig('centerline_plot.png')

plt.figure(figsize=(10, 6))
plt.plot(x_smooth, curvature, label="Curvature")
plt.xlabel("X")
plt.ylabel("Curvature")
plt.title("Curvature Along the Centerline")
plt.legend()
plt.grid(True)
plt.savefig('curvature_plot.png')
