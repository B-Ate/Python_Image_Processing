# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:03:58 2020

@author: Burak Atestepe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("hw_25000.csv")
#print(data.columns)



boy = data.Height.values.reshape(-1,1)
kilo = data.Weight.values.reshape(-1,1)

regression = LinearRegression()
regression.fit(boy,kilo)
print(regression.predict([[71]]))

x= np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
print(x)


plt.plot(x,regression.predict(x),color="red")
plt.scatter(data.Height,data.Weight)
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Simple Linear Regression")
plt.show()

print(r2_score(kilo,regression.predict(boy)))