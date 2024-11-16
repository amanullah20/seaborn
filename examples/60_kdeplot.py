 #Example: 60

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex")
g.map(sns.kdeplot, "total_bill", fill=True)
plt.show()
