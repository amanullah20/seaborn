#Example: 80

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=data, kind="kde", color="m")
plt.show()
