#Example: 50

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex", hue="day")
g.map(sns.kdeplot, "total_bill", fill=True, alpha=0.4).add_legend()
plt.show()
