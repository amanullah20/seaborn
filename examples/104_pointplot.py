#Example: 104

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.pointplot(x="day", y="total_bill", data=data)
plt.show()
