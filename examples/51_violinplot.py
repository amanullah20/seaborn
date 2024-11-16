#Example: 51

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="time", row="sex")
g.map(sns.violinplot, "total_bill", "day")
plt.show()
