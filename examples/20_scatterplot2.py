#Example: 20

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", hue="time", data=data)
plt.annotate("High Tip", xy=(40, 6), xytext=(25, 9), arrowprops=dict(facecolor="black", arrowstyle="->"))
plt.show()
