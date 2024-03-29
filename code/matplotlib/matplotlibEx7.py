import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d
ax = plt.subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, linewidth=0.2, color="red")
plt.show()