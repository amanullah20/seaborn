#Example: 94

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
sns.lineplot(x="year", y="passengers", hue="month", style="month", data=data)
plt.show()
