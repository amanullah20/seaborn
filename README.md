<h2 align=center>Overview of Seaborn</h2>
Seaborn is a Python data visualization library based on Matplotlib, and it provides a high-level
interface for drawing attractive and informative statistical graphics. Seaborn is specifically designed
for working with Pandas DataFrames and makes it easy to visualize complex relationships between
data, including summary statistics and distributions.

While Matplotlib provides a lot of flexibility and control over visualizations, Seaborn simplifies the
process of creating complex plots by abstracting away much of the low-level configuration needed in
Matplotlib.
### Key Features of Seaborn
1. **Built-in Statistical Plots:**
- Seaborn makes it easy to create statistical visualizations like heatmaps, box plots, violin plots,
pair plots, and regression plots.

**2. Integration with Pandas:**
- Seaborn is designed to work directly with Pandas DataFrames, allowing you to easily pass
DataFrame columns into plotting functions, which is convenient for data analysis.

**3. Themes and Color Palettes:**
- Seaborn provides built-in themes and color palettes to make your plots more visually
appealing without extensive configuration.

**4. Automatic Plotting of Summary Statistics:**
- Seaborn can automatically calculate and plot summary statistics (e.g., means, medians,
confidence intervals) for many types of plots.

**5. Categorical Plots:**
- Seaborn provides several specialized plot types like box plots, violin plots, strip plots, bar
plots, and count plots that are ideal for visualizing categorical data.

**6. Pairwise Relationships:**
- Pair plots and joint plots in Seaborn allow you to easily visualize relationships between
multiple variables.

**7. Heatmaps and Clustermaps**

- Seaborn offers powerful visualization tools for visualizing matrices or 2D data, such as
heatmaps and clustermaps.
### Basic Plotting with Seaborn
**1. Installation**

Seaborn can be installed via pip or conda:

```bash
pip install seaborn
```
### 2. Simple Line Plot
Seaborn's lineplot() function is used to create a line plot. It automatically calculates confidence
intervals for the mean of the data.
```bash
import seaborn as sns
import matplotlib.pyplot as plt
# Example data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
# Create a Seaborn line plot
sns.lineplot(x=x, y=y)
# Add titles and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```
### 3. Scatter Plot

Seaborn makes it easy to create scatter plots with the scatterplot() function.
```bash
# Scatter plot
sns.scatterplot(x=x, y=y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

### 4. Bar Plot
A bar plot is ideal for showing comparisons between categories. sns.barplot() computes and
displays the mean of each category by default.
```bash
import numpy as np
import pandas as pd
# Example data
df = pd.DataFrame({
'Category': ['A', 'B', 'C', 'D'],
'Value': [3, 6, 2, 5]
})
# Bar plot
sns.barplot(x='Category', y='Value', data=df)
plt.title('Bar Plot')
plt.show()
```
### 5. Histogram
Seaborn's histplot() function is a flexible function for creating histograms and kernel density
estimates (KDE).
```bash
# Example data
data = np.random.randn(1000)
# Histogram with KDE
sns.histplot(data, kde=True)
plt.title('Histogram with KDE')
plt.show()
```
### 6. Box Plot
Box plots are useful for visualizing the distribution of data, including quartiles and potential outliers.
```bash
# Box plot
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Box Plot')
plt.show()
```
### Advanced Plotting Technique

**1. Heatmap**
Heatmaps are useful for visualizing matrices or 2D data. Seaborn’s heatmap() function makes it easy
to display a matrix of values.
```bash
# Example data: Correlation matrix
data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap='Blues')
plt.title('Heatmap')
plt.show()
```
**2. Violin Plot**
A violin plot combines aspects of box plots and kernel density plots. It shows the distribution of the
data, including the probability density.
```bash
# Violin plot
sns.violinplot(x='Category', y='Value', data=df)
plt.title('Violin Plot')
plt.show()
```
**3. Pair Plot**
Pair plots allow you to visualize pairwise relationships between multiple variables in a dataset. It's a
great way to look at correlations and distributions at the same time.
```bash
# Example DataFrame with multiple numerical columns
df = pd.DataFrame({
'A': np.random.rand(100),
'B': np.random.rand(100),
'C': np.random.rand(100),
})
# Pair plot
sns.pairplot(df)
plt.show()
```bahs
4. Joint Plot
A joint plot visualizes the relationship between two variables, along with their individual distributions.
You can also plot a regression line or KDE
```bash
# Example data
df = pd.DataFrame({
'X': np.random.rand(100),
'Y': np.random.rand(100)
})
# Joint plot with scatter
sns.jointplot(x='X', y='Y', data=df, kind='scatter')
plt.show()
```
**5. FacetGrid**
Seaborn's FacetGrid allows you to create multiple subplots with shared axes based on different
categorical levels. This is useful for exploring relationships across multiple subsets of your data.
```bash
# Example data: Titanic dataset
df = sns.load_dataset('titanic')
# FacetGrid by 'class'
g = sns.FacetGrid(df, col='class', height=5)
g.map(sns.histplot, 'age')
plt.show()
```
**6. Regplot (Regression Plot)**
A regression plot allows you to visualize the relationship between two variables, along with a fitted
regression line.
```bash
# Regression plot
sns.regplot(x='X', y='Y', data=df)
plt.title('Regression Plot')
plt.show()
```
### Customization in Seaborn

**1. Themes and Color Palettes**
Seaborn has built-in themes and color palettes to make your plots visually appealing. You can change
the overall aesthetic using the set_theme() function
```bash

# Set a dark grid style theme
sns.set_theme(style="darkgrid")
# Create a plot
sns.lineplot(x=x, y=y)
plt.show()
```
You can also use Seaborn's built-in color palettes like 'deep' , 'muted' , 'dark' , 'colorblind' , etc.
```bash
# Use a color palette
sns.set_palette("husl")
# Plot data
sns.scatterplot(x=x, y=y)
plt.show()
```
**2. Adding Annotations**
You can add annotations to your plots using Matplotlib's annotate() function.
```bash
# Example data
df = pd.DataFrame({
'X': [1, 2, 3],
'Y': [3, 2, 5]
})
sns.scatterplot(x='X', y='Y', data=df)
# Annotate a point
plt.annotate('Point 1', xy=(1, 3), xytext=(1.5, 4),
arrowprops=dict(facecolor='blue', arrowstyle='->'))
plt.show()
```
**3. Multiple Plots Using FacetGrid or PairGrid**
Seaborn provides high-level interfaces like FacetGrid or PairGrid for creating grids of plots based
on specific categories.
```bash
# Example of a PairGrid
g = sns.PairGrid(df)
g.map_upper(sns.kdeplot, cmap='Blues')
g.map_lower(sns.scatterplot)
g.map_diag(sns.histplot, kde_kws={'color': 'black'})
plt.show()
```
### Summary of Key Seaborn Functions
```bash
Plot Type Seaborn Function Description

`Line Plot` sns.lineplot() Visualize a continuous variable.

`Scatter
Plot` sns.scatterplot() Visualize relationships between two variables.

`Bar Plot` sns.barplot() Display categorical data with bars.

`Histogram` sns.histplot() Show the distribution of a single variable.

`Box Plot` sns.boxplot() Display the distribution of a categorical variable.

`Violin Plot` sns.violinplot()

Visualize the distribution with a combination of box and
density plots.

`Pair Plot` sns.pairplot() Pairwise relationships between multiple variables.
```
| Heatmap | sns.heatmap() | Visualize matrices and 2D data. | | Joint Plot | sns.jointplot() |
Visualize relationships and distributions of two variables. | | FacetGrid | sns.FacetGrid() | Grid of
subplots based on categorical values. | | Regression Plot | sns.regplot() | Plot the regression line
between two variables. |

### Official Documentation
For more details on Seaborn's functions and their parameters, you can refer to the official
documentation:

[Documentation](https://seaborn.pydata.org/)
