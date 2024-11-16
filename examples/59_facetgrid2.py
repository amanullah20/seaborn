#Example: 59

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex")
g.map(sns.stripplot, "day", "total_bill", jitter=True)
plt.show()
