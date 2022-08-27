import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read csv
data= pd.read_csv("./Salary_Data.csv")
print(data)
data= np.array(data)
x = data[:, 0]
x= x.reshape(30,1)
print(x)
y = data[:, 1].reshape(30, 1)
"""plt.scatter(x, y, s=2)
plt.show()"""
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size= 0.2)
# scaler
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
scaler_y = StandardScaler()

sc_train_x = scaler_x.fit_transform(train_x)
sc_train_y = scaler_y.fit_transform(train_y)
print(sc_train_x )
print(sc_train_y )
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(sc_train_x, sc_train_y)
from sklearn.metrics import mean_squared_error
sc_test_x = scaler_x.transform(test_x)
sc_test_y = scaler_y.transform(test_y)
y_hat = regression.predict(sc_test_x)
print(f"evaluation MSE: {mean_squared_error(sc_test_y, y_hat)}")
Y_hat = regression.predict(scaler_x.transform(x))
Y_inv_hat = scaler_y.inverse_transform(Y_hat)
plt.scatter(x, y, s =3)
plt.plot(x, Y_inv_hat, color="red")
plt.show()