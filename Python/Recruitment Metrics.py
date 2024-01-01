import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from tabulate import tabulate
from sklearn.preprocessing import StandardScaler
df=pd.read_excel(r"D:\CIT\SEM-V\17MDC55 Files\Data.xlsx",sheet_name="Recruitment")
df.head()
df.groupby('Role')['Hired or Not'].sum()
df1=df.iloc[:,2:]
cor=df1.corr()
plt.figure(figsize=(5,5))
sb.heatmap(cor,cmap="coolwarm" , annot = True)
plt.show()

