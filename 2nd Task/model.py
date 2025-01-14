# -*- coding: utf-8 -*-
"""Task2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/113krLnr7SRXO3IVUiP8_4i_5DeB05rIF
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Unemployment in India.csv')
data = data.dropna()
print(data.head(5))

data.columns = data.columns.str.strip()
data.columns

features_to_normalize = ['Estimated Unemployment Rate (%)', 'Estimated Employed',
                          'Estimated Labour Participation Rate (%)']

scaler = StandardScaler()
normalized_features = scaler.fit_transform(data[features_to_normalize])

sns.set(style="whitegrid")
#Time Series Plot of Unemployment Rate
plt.figure(figsize=(10, 5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=data, marker='o')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(normalized_features)

print(data[['Region', 'Estimated Unemployment Rate (%)', 'Estimated Employed',
            'Estimated Labour Participation Rate (%)', 'Cluster']].head())

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Estimated Unemployment Rate (%)', y='Estimated Employed',
                hue='Cluster', palette='Set1', data=data, alpha=0.6)
plt.title('K-Means Clustering of Unemployment Data')
plt.xlabel('Estimated Unemployment Rate (%)')
plt.ylabel('Estimated Employed')
plt.legend(title='Cluster')
plt.tight_layout()
plt.show()