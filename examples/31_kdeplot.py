#Example: 31

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.kdeplot(data=data, x="sepal_length", y="sepal_width", hue="species", fill=True)
plt.show()