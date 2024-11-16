#Example: 61

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
sns.lineplot(x="year", y="passengers", data=data, palette="Blues")
plt.show()
