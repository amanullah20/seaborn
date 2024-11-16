#Example: 73

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.stripplot(x="day", y="total_bill", hue="sex", data=data, dodge=True, palette={"Male": "blue", "Female": "orange"})
plt.show()
