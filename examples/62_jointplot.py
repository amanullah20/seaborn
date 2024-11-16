#Example: 62

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.jointplot(x="total_bill", y="tip", data=data, marginal_kws=dict(bins=15, fill=True))
plt.show()
