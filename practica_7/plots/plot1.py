import matplotlib.pyplot as plt
import numpy as np

# Set limits
xmin = -4
xmax = 10
ymin = -2
ymax = 12

# Define the parameters
k = np.linspace(0, 10, 100)  # Range of k values
x = k * 1 + (-2)  # x-coordinate of the segment
y = k * 2 + 3  # y-coordinate of the segment

# Plotting
fig, ax = plt.subplots()
ax.plot(x, y, color='cornflowerblue', linewidth=2.5)  # Adjust color and linewidth

# Set the aspect ratio and limits
ax.set_aspect('equal')
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

# Set the grid
ax.grid(True, linestyle='--')

# Set the ticks
ax.set_xticks(np.arange(xmin, xmax+0.01, 2))
ax.set_yticks(np.arange(ymin, ymax+0.01, 2))

# Set the arrow for the x-axis
ax.annotate('', xy=(xmax, 0), xytext=(xmin, 0),
            arrowprops=dict(arrowstyle='->'))

# Set the arrow for the y-axis
ax.annotate('', xy=(0, ymax), xytext=(0, ymin),
            arrowprops=dict(arrowstyle='->'))

# Add text "y" at (-2, ymax - offset)
offset = 0.5
ax.text(-offset, ymax - offset, 'y', ha='right', va='center')

# Add text "x" at (xmax - offset, -2)
ax.text(xmax - offset, -offset, 'x', ha='center', va='top')

# Save the plot with minimal margins/padding
# plt.show()
plt.savefig('plot1.png', bbox_inches='tight')

