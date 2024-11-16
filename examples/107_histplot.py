#Example: 107

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("titanic")
sns.histplot(data, y="age", hue="sex", multiple="dodge", shrink=0.8)
plt.show()
