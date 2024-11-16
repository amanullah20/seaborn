#Example: 98

import seaborn as sns; import matplotlib.pyplot as plt
import numpy as np
data1 = np.random.rand(10, 10)
data2 = np.random.rand(10, 10)
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
sns.heatmap(data1, ax=axs[0], cmap="YlGnBu")
sns.heatmap(data2, ax=axs[1], cmap="coolwarm")
plt.show()
