#Example: 106

import matplotlib.pyplot as plt
import numpy as np
r = np.random.rand(100)
theta = 2 * np.pi * r
plt.figure(figsize=(6, 6))
plt.subplot(projection="polar")
plt.scatter(theta, r, alpha=0.75)
plt.show()
