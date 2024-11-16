#Example: 78

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.stripplot(x="day", y="total_bill", data=data, jitter=True)
plt.show()
