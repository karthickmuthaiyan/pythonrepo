import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataframe
data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Calculate the correlation matrix
corr = data.corr()

# Create a heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')

# Show the plot
plt.show()