#Example: 99

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="sex", data=data, dodge=True)
plt.show()
