# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:53:55 2020

@author: Burak Atestepe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

data = pd.read_csv("positions.csv")
print(data.columns)
print(data.describe())

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = LinearRegression()
regression.fit(level,salary)

tahmin = regression.predict([[8.3]])
# =============================================================================
# 
# plt.plot(level,regression.predict(level),color="red")
# plt.scatter(level,salary)
# plt.xlabel("Seviye")
# plt.ylabel("Maaş")
# plt.title("Simple Linear Regression")
# plt.show()
# =============================================================================

regressionPoly = PolynomialFeatures(degree=4)
levelPoly = regressionPoly.fit_transform(level)
regression2 = LinearRegression()
regression2.fit(levelPoly,salary)

tahmin2 = regression2.predict(regressionPoly.fit_transform([[8.3]]))

 plt.scatter(level,salary)
plt.plot(level,regression2.predict(levelPoly),color="red")
plt.plot(level,regression.predict(level),color="red")

plt.xlabel("Seviye")
plt.ylabel("Maaş")
plt.title("Simple Poly Regression")
plt.show()
