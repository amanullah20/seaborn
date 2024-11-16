#Example: 24

import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=data)
total = len(data)
for p in ax.patches:
    percentage = f"{100 * p.get_height() / total:.1f}%"
    ax.annotate(percentage, (p.get_x() + p.get_width() / 2., p.get_height()), ha="center", va="center")
plt.show()
