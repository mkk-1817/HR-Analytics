import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from tabulate import tabulate
from sklearn.preprocessing import StandardScaler
df=pd.read_excel(r"D:\CIT\SEM-V\17MDC55 Files\Data.xlsx",sheet_name="BARS and HCRI",header=1)
df.head()
df.groupby('Position')['Completed Training'].sum()
df1=df[['Age','Experience','Completed Training','Score']]
cor=df1.corr()
plt.figure(figsize=(5,5))
sb.heatmap(cor,cmap="coolwarm" , annot = True)
plt.show()

