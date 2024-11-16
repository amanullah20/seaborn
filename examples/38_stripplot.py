#Example: 38

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.stripplot(x="day", y="total_bill", data=data, jitter=0.3)
plt.show()
