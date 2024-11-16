#Example: 79

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=data, kind="hex", marginal_kws=dict(bins=20, fill=True))
sns.kdeplot(x=data["total_bill"], y=data["tip"], color="red")
plt.show()
