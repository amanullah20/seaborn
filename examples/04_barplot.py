#Example: 04

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=data, ci="sd")
plt.show()
