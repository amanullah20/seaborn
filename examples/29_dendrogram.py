 #Example: 29

import seaborn as sns; import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
data = np.random.rand(10, 4)
linked = linkage(data, 'single')
dendrogram(linked)
plt.show()
