#Example: 49

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex")
g.map(sns.kdeplot, "total_bill")
plt.show()
