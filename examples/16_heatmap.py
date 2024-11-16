#Example: 16

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.heatmap(data.pivot_table(index="day", columns="time", values="total_bill", aggfunc="mean"), annot=True, cmap="YlGnBu")
plt.show()
