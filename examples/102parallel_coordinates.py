#Example: 102

import pandas as pd; import seaborn as sns; import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
data = sns.load_dataset("iris")
parallel_coordinates(data, "species", color=("#556270", "#4ECDC4", "#C7F464"))
plt.show()
