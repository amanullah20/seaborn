#Example: 43

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
sns.lineplot(x="year", y="passengers", data=data, ci="sd")
plt.show()
