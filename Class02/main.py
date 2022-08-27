import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""dic = {"Sports":["Basketball", "Soccer", "Tennis", "Volleyball", "Badminton"],
       "Fruits":["Watermelon", "Banana", "Apple", "Lemon", "Strawberry"],
       "Animals": ["Monkey", "Ape", "Dog", "Cat", "Lion"]}
data = pd.DataFrame(dic)
#print(data)
data["Name"] = ["Thousand", "Allie", "John", "Michale", "Frank"]
#print(data)
data = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv")

data.head(5)

#print(data.iloc[0:5, 1:3])
data.sort_values(["HP"], ascending=True)
data = data.drop(columns=["#"])
print(data)
x= [1,2,3,4,5,1]
y= [6,3,2,5,7,6]
y2= [3,2,5,6,7,9]
plt.plot(x,y, marker="*", linestyle="--", label="A")
plt.plot(x,y2,label="B")
plt.legend()
plt.show()"""
"""ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
      84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
      78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

plt.plot(ages, py, color = 'red', label = 'Python')
plt.plot(ages, js, color = 'blue', label = 'Javascript')
plt.title("Median Salary (USD) by Age", fontdict={'fontname': 'Arial Black', 'fontsize': 16})
plt.xlabel("Ages", fontdict={'fontname': 'Arial Black', 'fontsize': 16})
plt.ylabel("Median Salary (USD)", fontdict={'fontname': 'Arial Black', 'fontsize': 16})
plt.legend()
plt.savefig('Median-salary.png')
plt.show()"""

"""slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.show()"""
"""x=[1,2,3,4,5,5,5,5,2,2,3,3,1]
plt.hist(x)"""
x = np.random.normal(0, 1, 10000)
plt.hist(x, bins=10)
plt.show()