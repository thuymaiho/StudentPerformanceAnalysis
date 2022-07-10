import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'D:\Data Analysis\StudentsPerformance.csv')
data.head()
data.shape
data.isnull().sum()
data.dtypes
data['gender'].value_counts()
data['parental level of education'].value_counts()
data['race/ethnicity'].value_counts()
data['lunch'].value_counts()
data['test preparation course'].value_counts()
data['total'] = data['math score'] + data['reading score'] + data['writing score']
data['average'] = data['total'] / 3
sns.distplot(data['math score'])
sns.distplot(data['reading score'])
sns.distplot(data['writing score'])
sns.distplot(data['average'])
sns.pairplot(data)
sns.barplot(data['race/ethnicity'], data['average'])
sns.barplot(data['parental level of education'], data['average'])

data['parental level of education'][data['average'] == min(data['average'])]
data['parental level of education'][data['average'] == max(data['average'])]
sns.barplot(data['test preparation course'], data['average'])

data['math_PassStatus'] = np.where(data['math score'] < 50, 'F', 'P')
data['read_PassStatus'] = np.where(data['reading score'] < 50, 'F', 'P')
data['write_PassStatus'] = np.where(data['writing score'] < 50, 'F', 'P')
data.head()
p = sns.countplot(x='parental level of education', data=data, hue='math_PassStatus', palette='bright')
p = plt.setp(p.get_xticklabels(), rotation=90)
p1 = sns.countplot(x='test preparation course', data=data, hue='math_PassStatus', palette='bright')
p1 = plt.setp(p.get_xticklabels(), rotation=90)
p2 = sns.countplot(x='parental level of education', data=data, hue='read_PassStatus', palette='bright')
p2 = plt.setp(p.get_xticklabels(), rotation=90)
p3 = sns.countplot(x='test preparation course', data=data, hue='read_PassStatus', palette='bright')
p3 = plt.setp(p.get_xticklabels(), rotation=90)
p4 = sns.countplot(x='parental level of education', data=data, hue='write_PassStatus', palette='bright')
p4 = plt.setp(p.get_xticklabels(), rotation=90)
p5 = sns.countplot(x='test preparation course', data=data, hue='write_PassStatus', palette='bright')
p5 = plt.setp(p.get_xticklabels(), rotation=90)