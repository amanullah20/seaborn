#Example: 89

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.lmplot(x="total_bill", y="tip", data=data, logx=True)
plt.show()
