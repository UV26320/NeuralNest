# -*- coding: utf-8 -*-
"""Simple Linear Regression_part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ADNziInXySdBVgSTcge21paFYKjeCRE1
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('placement.csv')

df.head()

plt.scatter(df['cgpa'],df['package'])
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')

X = df.iloc[:,0:1]
y = df.iloc[:,-1]

y

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,y_train)

X_test

y_test

lr.predict(X_test.iloc[0].values.reshape(1,1))

plt.scatter(df['cgpa'],df['package'])
plt.plot(X_train,lr.predict(X_train),color='red')
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')

m = lr.coef_

b = lr.intercept_

# y = mx + b

m * 8.58 + b

m * 9.5 + b

m * 100 + b

