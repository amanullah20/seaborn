#Example: 139

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=data, inner="quartile")
plt.show()
