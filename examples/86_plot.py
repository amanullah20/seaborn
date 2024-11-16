#Example: 86

import seaborn as sns; import matplotlib.pyplot as plt
import pandas as pd
data = pd.Series(sns.load_dataset("flights")["passengers"])
pd.plotting.lag_plot(data)
plt.show()
