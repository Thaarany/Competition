import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
df = pd.read_csv("D:\muuruga sem3 pass annum\healthcare-dataset-stroke-data.csv")
df.head()
print(df.isna().sum())
df.isna().sum().plot.barh(color='skyblue')

# Add title and labels for clarity
plt.title('Missing Values by Column')
plt.xlabel('Number of Missing Values')
plt.ylabel('Columns')

plt.show()
df.describe()
