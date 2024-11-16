#Example: 88

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
sns.regplot(x="year", y="passengers", data=data, ci=None)
plt.show()
