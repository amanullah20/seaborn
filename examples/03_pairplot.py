#Example:03

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.pairplot(data, hue="species", markers=["o", "s", "D"])
plt.suptitle("Pair Plot with Annotations", y=1.02)
plt.show()
