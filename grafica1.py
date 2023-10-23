
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, np.pi, 100)

x = np.cos(theta)
y = -np.sin(theta)

sizes = np.linspace(100, 100, 100)  

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.scatter([-0.3, 0.3], [-0.2, -0.2], c='black', s=400, alpha=1) 

plt.scatter([0], [-0.5], c='red', s=20, alpha=1) 

plt.show()