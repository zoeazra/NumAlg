import matplotlib.pyplot as plt
import numpy as np

# Define a nonlinear equation (curve)
x = np.linspace(-3, 3, 400)
y_nonlinear = x**2 - 2  # Example of a parabolic curve (nonlinear)

# Define a linear equation (line)
y_linear = 0.5 * x + 1  # Example of a straight line (linear)

# Plot both curves
plt.figure(figsize=(10, 6))

# Plot nonlinear curve
plt.plot(x, y_nonlinear, label='Nonlinear: $y = x^2 - 2$', linewidth=2)

# Plot linear curve
plt.plot(x, y_linear, label='Linear: $y = 0.5x + 1$', linestyle='--', linewidth=2)

# Add labels, legend, and grid
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Comparison of Nonlinear and Linear Equations")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
