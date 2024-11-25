#Example: 126

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="sex", data=data)
plt.show()
