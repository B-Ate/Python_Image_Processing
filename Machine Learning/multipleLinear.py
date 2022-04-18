# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:37:55 2020

@author: Burak Atestepe
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("insurance.csv")
print(data.columns)
print(data.describe())

##y ekseni
expenses = data.expenses.values.reshape(-1,1)

## x ekseni
ageBmis = data.iloc[:,[0,2]].values

regression = LinearRegression()
regression.fit(ageBmis,expenses)

print(regression.predict([[20,20],[20,25]]))
      
      
      
# =============================================================================
# boy = data.Height.values.reshape(-1,1)
# kilo = data.Weight.values.reshape(-1,1)
# 
# regression = LinearRegression()
# regression.fit(boy,kilo)
# print(regression.predict([[71]]))
# 
# x= np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
# print(x)
# 
# 
# plt.plot(x,regression.predict(x),color="red")
# plt.scatter(data.Height,data.Weight)
# plt.xlabel("Boy")
# plt.ylabel("Kilo")
# plt.title("Simple Linear Regression")
# plt.show()
# 
# print(r2_score(kilo,regression.predict(boy)))
# =============================================================================
