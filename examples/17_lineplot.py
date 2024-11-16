#Example: 17

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
sns.lineplot(x="year", y="passengers", hue="month", data=data, ci="sd")
plt.show()
