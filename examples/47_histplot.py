#Example: 47

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
g = sns.FacetGrid(data, hue="species", aspect=1.5)
g.map(sns.histplot, "sepal_length", kde=True).add_legend()
plt.show()
