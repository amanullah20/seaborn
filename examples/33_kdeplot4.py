#Example: 33

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.kdeplot(x="total_bill", y="tip", hue="day", data=data, fill=True, alpha=0.3)
plt.show()
