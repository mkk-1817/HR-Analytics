import pandas as pd
import statsmodels.api as sm
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df=pd.read_excel(r"D:\CIT\SEM-V\17MDC55 Files\Data.xlsx",sheet_name="BARS and HCRI",header=1)
df.head()
x=df[['Age','Experience']]
y=df['Salary']
reg=LinearRegression()
reg.fit(x,y)
age=float(input("Enter age:"))
we=float(input("Enter experience:"))
sal=reg.predict([[age,we]])
print("Expected salary:",int(sal))
df1=df[['Age','Experience','Salary']]
cor=df1.corr()
plt.figure(figsize=(5,5))
sb.heatmap(cor,cmap="coolwarm" , annot = True)
plt.show()
