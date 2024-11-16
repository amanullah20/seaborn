#Example: 36

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.heatmap(data.corr(), cmap=sns.diverging_palette(220, 20, as_cmap=True), annot=True)
plt.show()
