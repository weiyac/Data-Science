import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("advertising.csv")
x = np.array(data[["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage", "Male"]])
y = np.array(data["Clicked on Ad"])
train_x, test_x, train_y, test_y  = train_test_split(x, y, test_size=0.2, random_state=10)
scaler_x = StandardScaler()
sc_train_x = scaler_x.fit_transform(train_x)
logistic = LogisticRegression()
logistic.fit(sc_train_x,train_y)
sc_test_x = scaler_x.transform(test_x)
y_hat = logistic.predict(sc_test_x)
print(confusion_matrix(test_y, y_hat))
print(logistic.score(X=sc_test_x, y= test_y))
