#Example: 56

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex")
g.map(sns.pointplot, "day", "total_bill", order=["Thur", "Fri", "Sat", "Sun"])
plt.show()
