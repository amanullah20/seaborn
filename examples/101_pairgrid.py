 #Example: 101

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.PairGrid(data, hue="sex")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()
