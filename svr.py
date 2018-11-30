import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')

data = data.iloc[:,1:13]

X = data.iloc[: ,:-1].values
Y = data.iloc[: , -1].values


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_y.fit_transform(Y)

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, Y)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df


y_pred = regressor.predict(X_test)
y_pred = sc_y.inverse_transform(y_pred)

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


import seaborn
seaborn.regplot(y_test,y_pred,data=None, x_estimator=None, x_bins=None, x_ci='ci', 
  scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False,
  lowess=False, robust=False, logx=False, x_partial=None, y_partial=None,
 truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color='black', 
 marker='o', scatter_kws=None, line_kws=None, ax=None)

from sklearn.metrics import mean_squared_error


mean_squared_error(y_test, y_pred)

