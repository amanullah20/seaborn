#Example: 64

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("titanic")
sns.stripplot(x="class", y="age", hue="sex", data=data, dodge=True, jitter=0.3)
plt.show()
