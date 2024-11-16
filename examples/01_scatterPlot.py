#Example: 01

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.scatterplot(x="sepal_length", y="sepal_width", data=data, s=100, edgecolor="black", linewidth=1.5)
plt.show()
