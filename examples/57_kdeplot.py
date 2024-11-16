#Example: 57

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
g = sns.FacetGrid(data, row="species", aspect=4, height=1.5)
g.map(sns.kdeplot, "sepal_length", fill=True)
plt.show()
