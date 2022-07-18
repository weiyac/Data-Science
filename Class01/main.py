import numpy as np
"""a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [3.2, 5.8, 6.9]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)"""
"""a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a[1, 2])
print(a[0, :])
print(a[:, 0])
print(a[0,1:5:2])
a[:, 2] = [10, 12]
print(a)"""
"""a = np.array([[[1, 2], [3, 4], [5, 6]],
              [[-1, -2], [-3, -4], [-5, -6]],
              [[1, 7], [5, 4], [6, 6]],
              [[1.3, 2], [3.7, 4], [5.2, 6]],
              [[1, -2], [3, -4], [5, -6]]])
print(a.shape)
print(a[:, 0:2, 1])
"""
"""a = np.zeros((3, 2))
print(a)
print(a.dtype)
b = np.ones((2, 5), dtype=np.int32)
print(b)
c = np.full((2,3), 100, dtype= np.float32)
print(c)"""

#shape
"""a = np.array([1, 2, 3, 4, 5])
print(a.shape)
b = np.array([[1], [2], [3], [4], [5]])
print(b.shape)
c = np.array([[1, 2, 3, 4, 5]])
print(c.shape)"""

"""x= np.random.rand(100,2)
y= np.random.randint(low=10, high=100, size=(3,2))
print(x)
print(y)
print(x[:, 0])
print(x[:, 1])
import matplotlib.pyplot as plt
plt.scatter(x[:, 0], x[:, 1], s=1, color= "red")
plt.show()"""

# reshape
"""x = np.random.rand(3, 4)
print(x)
x = x.reshape(4, 3)
print(x)
x = x.reshape(-1, 6)
print(x)"""

"""a = np.array([[1, 2, 3], [4, 5, 6]])
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)"""
"""a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)
x = np.array(a)
y = np.array(b)
print(x+y)"""

"""a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[2, 3, 1], [5, 2, 1]])
print(np.dot(a,b))"""

"""a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
identity = np.indentity(3)
print(np.matmul(a, identity))"""

"""a = np.array([[92, 83, 56, 77, 98], [81, 53, 64, 76, 60]])
print(np.max(a, axis = 0))
print(np.max(a, axis = 1)) # (2,5)
print(np.sum(a, axis = 0))
print(np.sum(a, axis = 1))"""

# pandas
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv")
print(data.head())
data = data.drop(columns=["#"])
print(data.head())
data.to_csv("pokemon.csv", index=False)