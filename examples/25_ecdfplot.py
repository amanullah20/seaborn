#Example: 25

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.ecdfplot(data=data, x="total_bill", hue="day")
plt.show()
