#Example: 100

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=data, order=["Thur", "Fri", "Sat", "Sun"])
plt.show()
