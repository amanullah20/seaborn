#Example: 07

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.histplot(data, x="total_bill", hue="day", multiple="fill", kde=True)
plt.show()
