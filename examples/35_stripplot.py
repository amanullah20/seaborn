#Example: 35

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
data["sepal_diff"] = data["sepal_length"] - data["sepal_width"]
sns.stripplot(x="species", y="sepal_diff", data=data, palette="coolwarm")
plt.axhline(0, color="gray", linestyle="--")
plt.show()
