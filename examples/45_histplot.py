#Example: 45

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="time")
g.map(sns.histplot, "total_bill")
plt.show()
