#Example: 96

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="time", data=data, palette="Set2")
plt.show()
