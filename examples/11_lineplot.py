#Example: 11

import seaborn as sns; import matplotlib.pyplot as plt
import pandas as pd
data = pd.DataFrame({"Year": ["2010", "2011", "2012", "2013"], "Rank A": [1, 2, 3, 1], "Rank B": [2, 1, 2, 3]})
sns.lineplot(x="Year", y="Rank A", marker="o", data=data)
sns.lineplot(x="Year", y="Rank B", marker="o", data=data)
plt.gca().invert_yaxis()
plt.show()
