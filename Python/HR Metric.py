import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
df=pd.read_excel(r"D:\CIT\SEM-V\17MDC55 Files\Data.xlsx",sheet_name="Data")
df.head()
print("Data description:")
df.describe()
df=df.drop_duplicates()
df[df.duplicated()]
#Null values check
print(df.isnull().sum())
df1=df.iloc[:,5:]
df1.head()
fnames=['Working Conditions','Relationship with Colleagues','Job Satisfaction','Companys Policy','Rewards and Awards','Workload and Support']
f_dict=dict()
for i in range(0,6):
    f_dict[fnames[i]]=df1.iloc[:,4*i+1:4*i+5].sum(axis=1)
fac_df=pd.DataFrame(f_dict)
fac_df.head()
fac_df["Score"]=fac_df.iloc[:,0:6].sum(axis=1)
mean=int(fac_df[["Score"]].mean())
fac_df.loc[fac_df['Score'] >= mean, 'Satisfaction'] = 'High'
fac_df.loc[fac_df['Score'] < mean, 'Satisfaction'] = 'Low'
count=fac_df["Satisfaction"].value_counts()
print(count)
cor=fac_df.iloc[:,0:6].corr()
plt.figure(figsize=(5,5))
sb.heatmap(cor,cmap="coolwarm" , annot = True)
plt.show()
linkage=hierarchy.linkage(cor,method='ward')
dendo=hierarchy.dendrogram(linkage,labels=cor.columns,orientation='top')
plt.xticks(rotation=90)
plt.title("Dendrogram of Correlation Matrix")
plt.show()
fac_df1=df[['ID', 'Name', 'Age', 'Experience', 'Position']].join(fac_df)
fac_df1['Position'].groupby(fac_df1['Satisfaction']).max()
fac_df1['Age'].groupby(fac_df1['Satisfaction']).max()

