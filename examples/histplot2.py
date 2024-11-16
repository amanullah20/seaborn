#Example: 74

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.histplot(data=data, x="total_bill", hue="sex", multiple="layer", cumulative=True, kde=True)
plt.show()
