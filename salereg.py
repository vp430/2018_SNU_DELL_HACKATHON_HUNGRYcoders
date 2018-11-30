import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.metrics import accuracy_score
data = pd.read_csv('data1.csv')

data = data.iloc[:,1:13]

'''
data.corr()

data.std()

data.describe()

data['Sales'].hist()

data.boxplot(column='Sales')'''

X = data.iloc[: ,:-1].values
Y = data.iloc[: , -1].values

'''
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
'''
# ENcoding the data 


# splitting into train and test 
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size = 0.2 ,random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.fit_transform(y_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

import statsmodels.formula.api as sm
model = sm.OLS(Y,X.astype(float)).fit()
model.summary()

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df

from sklearn.metrics import mean_squared_error


mean_squared_error(y_test, y_pred)


mean_squared_error(y_test, y_pred)  

import seaborn
seaborn.regplot(y_test,y_pred,data=None, x_estimator=None, x_bins=None, x_ci='ci', 
  scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False,
  lowess=False, robust=False, logx=False, x_partial=None, y_partial=None,
 truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color='black', 
 marker='o', scatter_kws=None, line_kws=None, ax=None)



