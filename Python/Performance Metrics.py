import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from tabulate import tabulate
from sklearn.preprocessing import StandardScaler
df=pd.read_excel(r"D:\CIT\SEM-V\17MDC55 Files\Data.xlsx",sheet_name="Performance")
df.head()
from sklearn.cluster import KMeans
scaled_df = df.iloc[:,1:]
scaled_df.head()
k_opt=2
model = KMeans(n_clusters=k_opt,random_state =42,n_init=104)
model.fit(scaled_df)
scaled_df['labels'] = model.labels_
cluster_centers = model.cluster_centers_
plt.figure(figsize=(8, 6))
plt.scatter(scaled_df['Experience'], scaled_df['Performance Score'] , c=scaled_df['labels'], cmap='coolwarm')
plt.title('K-means Clustering')
plt.xlabel('Experience')
plt.ylabel('Performance Score')
plt.show()
scaled_df.head()

