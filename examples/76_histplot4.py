#Example: 76

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.histplot(data, x="total_bill", hue="time", element="step", stat="density")
plt.show()
