import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dic = {"Sports":["Basketball", "Soccer", "Tennis", "Volleyball", "Badminton"],
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