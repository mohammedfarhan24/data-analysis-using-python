# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzYR1bmrFSNvErS9nQCJWRYRNz69ajLo
"""

import numpy as np
#creating arrays
arr=np.array([1,2,3,4,5])
print(arr)
a=np.zeros((3,3),dtype=int)
print(a)
b=np.ones((2,2),dtype=int)
print(b)
#arrange array
arangearr=np.arange(10)
print(arangearr)
#reshaped array
reshaped_arr=arr.reshape(5,1)
print(reshaped_arr)
#sliced array
sliced_arr=arr[2:4]
print(sliced_arr)
#addition of arrays
arr2=np.array([1,2,3])
arr1=np.array([6,7,8])
result=arr2+arr1
print(result)
#numpy manipulation vstack func
c=np.vstack(arr2+arr1)
print(c)
c=np.stack(arr2+arr1)
print(c)
#spliting fuctions
arr4=np.array([2,4,6,8,10,11,12])
f=np.split(arr4,3.5)
print(f)
#splitting method 2
arr5=np.array([1,2,3,4,5,6])
e=np.split(arr5,3)
print(e)
a=np.array([[1,2,3,4],[5,6,7,8]])
b=a.T
print(b)
#linear algebra with numpy
#seperate 2d 2x2 matrix
g=np.array([[2,5],[4,8]])
p=np.array([[3,6],[1,5]])
j=np.dot(g,p)
print(j)
d=np.linalg.eig(j)
print(d)
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=np.array([[7,8,9],[10,11,12]])
print(b)
#sum of arrays
c=np.sum([a+b])
print(c)
#statistical operations
o=np.array([1,2,3,4,5])
v=np.mean(o)
print(v)
k=np.median(o)
print(k)
l=np.var(o)
print(l)
h=np.std(o)
print(h)
data=np.loadtxt("/content/numbers.txt",dtype=int)
data=np.savetxt("/content/number.txt",data)
print(data)

#matplotlib library

import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5])
plt.plot(a)

!pip install numpy
#numpy library

import pandas as pd
a=['mahesh','sairam','lovaraju','kamal','dimpu','sai']
r=pd.Series(a,index=[1,2,3,4,5,6])
print(r)

import pandas as pd
df= pd.read_csv("/titanic.csv")
print(df)

xl= pd.read_excel("/content/HR_Employee_Data.xlsx")
print(xl)

pf= pd.read_csv("/content/data_science.txt",sep=" ")
print(pf)

xl= pd.read_excel("/content/HR_Employee_Data.xlsx")
print(xl)



#print in one row as series
print(xl.loc[1])

xl= pd.read_excel("/content/HR_Employee_Data.xlsx",sheet_name="HR_Employee_Data")
print(xl)

#print in one row as series
print(xl.loc[1])

import pandas as pd
dfn= pd.read_csv("/content/titanic.csv")
mv=dfn.drop_duplicates()
dfn.shape
a=dfn.head(10)
b=dfn.tail(10)
c=pd.concat([a,b], axis=0)
c.to_csv('rajesh.csv')

mv=dfn['PassengerId'].mean()
print(mv)

print(c.groupby(['PassengerId'])['Survived'].count())

#numpy library
#matplotlib library
#cricket
import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='orange')
plt.title('IndvsAus_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#generate array of 200 values between -pi & pi
lion=np.linspace(-2*np.pi,2*np.pi,100)
print(lion)
plt.plot(lion,np.sin(lion),color='blue')#SIN plt.plot(x,y,color,labels...
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
overs =np.arange(5,50,5)
overs_a=np.arange(5,30,5)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='India')
plt.subplot(2,1,1)

plt.plot(overs_a,runs_a,color='yellow',label='Aus')
plt.legend(loc='best')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='CompanyA',marker='>',ms='15',mec='k')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='CompanyB',marker='H')
plt.legend(loc='best')
plt.show()

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
c=['green','red','blue','yellow']
explo=[0.2,0,0,0]
plt.pie(a,labels= labe,explode=explo,startangle=180,colors=c,textprops={'fontsize':36})
plt.legend()
plt.show()

#Task1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset containing daily temperatures
# Assuming the dataset is in a CSV file named 'temperature_data.csv' with a column named 'temperature'
df = pd.read_csv('/content/city_temperature.csv')
print(df)


average_temperature = df['AvgTemperature'].mean()
highest_temperature = df['AvgTemperature'].max()
lowest_temperature = df['AvgTemperature'].min()
threshold = 30
days_above_threshold = df[df['AvgTemperature'] > threshold].shape[0]


print("Average temperature for the month:", average_temperature)
print("Highest temperature recorded:", highest_temperature)
print("Lowest temperature recorded:", lowest_temperature)
print("Number of days where temperature exceeded", threshold, "degrees Celsius:", days_above_threshold)
df.plot(kind='line',color='blue')
plt.title("Temperature for 50 days")
plt.xlabel("Days")
plt.ylabel("Temperature")

#seaborn library
import seaborn as sns
import matplotlib.pyplot as plt
tips= sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip",data=tips)
plt.title("Scatter Plot of total_bill vs tip")
plt.xlabel("total_bill($)")
plt.ylabel("tips($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips= sns.load_dataset("titanic")
print(tips)

# Plot the four datasets in the anscombe dataset
sns.scatterplot(x="survived", y="age", data=tips)
plt.title("scatter plot of survived vs age")
plt.xlabel("Survived")
plt.ylabel("age")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap of Iris dataset")
plt.show()
print(iris)

import seaborn as sns
import matplotlib.pyplot as plt
earth=sns.load_dataset("planets")
correlation_matrix=earth.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap of planets dataset")
plt.show()
print(earth)