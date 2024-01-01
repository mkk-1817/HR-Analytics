import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from tabulate import tabulate
from sklearn.preprocessing import StandardScaler
df=pd.read_excel(r"D:\CIT\SEM-V\17MDC55 Files\Data.xlsx",sheet_name="BARS and HCRI",header=1)
df.head()
df['Position'].groupby(df['BARS Level']).max()
df1={}
for pos in df['Position'].unique():
    pos_df=df[df['Position']==pos]
    df1[pos]=pos_df
k_df=pd.DataFrame(df1["KG Teacher"])
t_df=pd.DataFrame(df1["Teacher"])
o_df=pd.DataFrame(df1["Office Assistant"])
k_df['BARS Level']=k_df['BARS Level']
t_df['BARS Level']=t_df['BARS Level']
o_df['BARS Level']=o_df['BARS Level']
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
bars=k_df['BARS Level'].values
age=k_df['Age'].values
feat=np.column_stack((bars,age))
model=KMeans(n_clusters=2,n_init=10)
model.fit(feat)
label = model.predict(feat)
cluster_centers = model.cluster_centers_
k_df['Cluster'] = label
k_df['Cluster'].groupby(k_df['Cluster']).count()
plt.scatter(bars,age, c=label, cmap='rainbow')
plt.xlabel('BARS')
plt.ylabel('Age')
plt.show()
bars=o_df['BARS Level'].values
age=o_df['Age'].values
feat=np.column_stack((bars,age))
model=KMeans(n_clusters=2,n_init=10)
model.fit(feat)
label = model.predict(feat)
cluster_centers = model.cluster_centers_
o_df['Cluster'] = label
plt.scatter(bars,age, c=label, cmap='rainbow')
plt.xlabel('BARS')
plt.ylabel('Age')
plt.show()
o_df['Cluster'].groupby(o_df['Cluster']).count()
bars=t_df['BARS Level'].values
age=t_df['Age'].values
feat=np.column_stack((bars,age))
model=KMeans(n_clusters=2,n_init=10)
model.fit(feat)
label = model.predict(feat)
cluster_centers = model.cluster_centers_
t_df['Cluster'] = label
plt.scatter(bars,age, c=label, cmap='rainbow')
plt.xlabel('BARS')
plt.ylabel('Age')
plt.show()
t_df['Cluster'].groupby(t_df['Cluster']).count()

