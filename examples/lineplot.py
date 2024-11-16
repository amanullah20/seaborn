#Example: 40

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
fig, ax1 = plt.subplots()
sns.lineplot(x="year", y="passengers", data=data, ax=ax1)
ax2 = ax1.twinx()
sns.lineplot(x="year", y="passengers", data=data, color="r", ax=ax2)
plt.show()
