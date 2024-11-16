#Example: 27

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.ecdfplot(data["total_bill"])
plt.show()
