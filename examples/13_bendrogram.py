#Example: 13

import seaborn as sns; import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
data = sns.load_dataset("iris").drop(columns=["species"])
linkage_matrix = linkage(data, "ward")
dendrogram(linkage_matrix, truncate_mode="level", p=3)
plt.show()
