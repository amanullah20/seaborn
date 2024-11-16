#Example: 55

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
g = sns.PairGrid(data, hue="species")
g.map_diag(sns.kdeplot, fill=True)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()
