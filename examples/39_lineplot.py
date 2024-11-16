#Example: 39

import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("flights")
fig, ax1 = plt.subplots()
sns.lineplot(x="year", y="passengers", data=data, ax=ax1)
ax2 = ax1.twinx()
sns.lineplot(x="year", y="passengers", data=data, color="red", ax=ax2)
plt.show()
