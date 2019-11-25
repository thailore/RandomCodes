import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
prod_per_year = df.groupby('year').totalprod.mean().reset_index()

X = prod_per_year['year'].values.reshape(-1,1)
y = prod_per_year['totalprod']

# Create Linear Regression model using current data 1998-2012
regr = linear_model.LinearRegression()
regr.fit(X, y)
y_predict = regr.predict(X)

# Use model to predict data for 2013-2050
X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1,1)
future_predict = regr.predict(X_future)

plt.scatter(X, y)
plt.plot(X, y_predict)
plt.show()

plt.plot(X_future, future_predict)
plt.show()

print(regr.predict(np.array(2050))) # 186,545 predicted Honey production in year 2050
