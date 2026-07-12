import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


Automobile_data=pd.read_csv("Automobile_data.csv", na_values="?")


# print(Automobile_data.head())
# print(Automobile_data.tail())
# print(Automobile_data.shape)
# print(Automobile_data.columns)
Automobile_data.info()
# print(Automobile_data.describe())

print(Automobile_data.isnull().sum())

numer_cols=[
    "normalized-losses",
    "bore",
    "stroke",   
    "horsepower",
    "peak-rpm",
    "price"
]
for col in numer_cols:
    Automobile_data[col].fillna(Automobile_data[col].mean(), inplace=True)

Automobile_data["num-of-doors"].fillna(Automobile_data["num-of-doors"].mode()[0],inplace=True)
    
print("Duplicate rows:", Automobile_data.duplicated().sum())


Automobile_data=Automobile_data.drop_duplicates()

# print(Automobile_data.sort_values(by=Automobile_data.columns[0]).head())
# print(Automobile_data.corr(numeric_only=True))


