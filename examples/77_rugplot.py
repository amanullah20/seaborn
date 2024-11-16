#Example: 77

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.histplot(data["total_bill"], kde=True)
sns.rugplot(data["total_bill"], color="r")
plt.show()
