#Example: 75

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.histplot(data["total_bill"], bins=np.logspace(0.1, 2, 30))
plt.xscale("log")
plt.show()
