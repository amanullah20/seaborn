#Example: 92

import seaborn as sns; import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(10, 12)
sns.heatmap(data, cmap="YlGnBu")
plt.show()
