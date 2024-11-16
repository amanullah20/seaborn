 #Example: 44

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="time")
g.map(sns.kdeplot, "total_bill", fill=True)
plt.show()
