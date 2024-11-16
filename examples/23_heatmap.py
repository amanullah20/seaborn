#Example: 23

import seaborn as sns; import matplotlib.pyplot as plt
import numpy as np
data = sns.load_dataset("iris").iloc[:, :-1].corr()
mask = np.triu(np.ones_like(data, dtype=bool))
sns.heatmap(data, mask=mask, cmap="coolwarm", annot=True)
plt.show()
