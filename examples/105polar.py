#Example: 105

import seaborn as sns; import matplotlib.pyplot as plt
import numpy as np
data = sns.load_dataset("iris")
theta = np.linspace(0, 2*np.pi, len(data["sepal_length"]))
r = data["sepal_length"]
plt.polar(theta, r, marker="o", linestyle="None")
plt.show()
