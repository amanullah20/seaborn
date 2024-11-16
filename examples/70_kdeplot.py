#Example: 70

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=data, kind="hex")
sns.kdeplot(x=data["total_bill"], y=data["tip"], color="red")
plt.show()
