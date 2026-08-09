#Generating normal distribution
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

mean = 0 
std_dev = 1
size = 1000

data = np.random.normal(loc=mean, scale=std_dev, size = size)

print(np.mean(data))
print(np.median(data))
print(np.std(data))

#plot a histogram 
sns.histplot(data, kde=True)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal distribution')
plt.show()

df = pd.DataFrame(data, columns=['Vale'])
df['Z-score'] = (df['Value'] - df['Value'].mean()) /df['Value'].std()
df.head()

outliers = df[(df['Z-Score'] < -3) | (df['Z-Score'] > 3)]
outliers.head(10)

df_cleaned = df[(df['Z-Score'] >= -3) | (df['Z-Score'] <= 3)]
df_cleaned.shape
df.shape