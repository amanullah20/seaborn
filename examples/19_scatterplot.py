#Example: 19

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, row="sex", col="time")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()
