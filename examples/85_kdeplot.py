#Example: 85

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.kdeplot(data["total_bill"])
plt.show()
