#Example: 46

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="time", hue="sex")
g.map(sns.scatterplot, "total_bill", "tip").add_legend()
plt.show()
