#Example: 83

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.kdeplot(x="total_bill", y="tip", data=data)
plt.show()
