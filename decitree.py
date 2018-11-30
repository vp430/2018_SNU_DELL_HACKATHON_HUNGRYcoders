import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')

data = data.iloc[:,1:13]

X = data.iloc[: ,:-1].values
Y = data.iloc[: , -1].values





from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4, random_state = 0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)


y_pred = regressor.predict(X_test)


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df


import seaborn
seaborn.regplot(y_test,y_pred,data=None, x_estimator=None, x_bins=None, x_ci='ci', 
  scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False,
  lowess=False, robust=False, logx=False, x_partial=None, y_partial=None,
 truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color='black', 
 marker='o', scatter_kws=None, line_kws=None, ax=None)

from sklearn.metrics import mean_squared_error


mean_squared_error(y_test, y_pred)
