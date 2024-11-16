#Example: 93

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=data)
plt.show()
