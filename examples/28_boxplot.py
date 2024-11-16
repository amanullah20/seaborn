#Example: 28

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=data, order=["Sun", "Sat", "Fri", "Thur"])
plt.show()
