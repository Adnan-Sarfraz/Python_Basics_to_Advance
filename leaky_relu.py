import numpy as np
import matplotlib.pyplot as plt

# Define Leaky ReLU
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Generate input values
x = np.linspace(-10, 10, 400)
y = leaky_relu(x)

# Plotting Leaky ReLU
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Leaky ReLU', color='orange')
plt.title("Leaky ReLU Activation Function")
plt.xlabel("Input (x)")
plt.ylabel("Output f(x)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
