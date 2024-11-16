#Example: 37

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.pointplot(x="day", y="total_bill", hue="sex", data=data, capsize=.2)
plt.show()
