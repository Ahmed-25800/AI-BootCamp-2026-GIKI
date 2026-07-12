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

print(Automobile_data.sort_values(by=Automobile_data.columns[0]))

filtered_data = [
    Automobile_data[Automobile_data["price"] > 20000],
    Automobile_data[Automobile_data["fuel-type"] == "gas"],
    Automobile_data[Automobile_data["horsepower"] > 100]
]
print(filtered_data[0].shape)
# Average price by manufacturer

Automobile_data.groupby("make")["price"].mean()


# Average price by fuel type
Automobile_data.groupby("fuel-type")["price"].mean()

# Average price by body style
Automobile_data.groupby("body-style")["price"].mean()

# Count of cars by manufacturer
Automobile_data.groupby("make").size()

# Summary statistics
Automobile_data.groupby("fuel-type")["price"].agg(
    ["count", "mean", "min", "max"]
)

plt.figure(figsize=(8,5))
plt.hist(Automobile_data["price"], bins=15, edgecolor="black")
plt.title("Distribution of Car Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig("Histogram_Price.png")
plt.show()


avg_price_fuel = Automobile_data.groupby("fuel-type")["price"].mean()

plt.figure(figsize=(6,5))
avg_price_fuel.plot(kind="bar")
plt.title("Average Price by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average Price")
plt.savefig("Bar_FuelType.png")
plt.show()


avg_price_make = Automobile_data.groupby("make")["price"].mean()

plt.figure(figsize=(12,5))
avg_price_make.plot(kind="line", marker="o")
plt.title("Average Price by Manufacturer")
plt.xlabel("Manufacturer")
plt.ylabel("Average Price")
plt.xticks(rotation=90)
plt.savefig("Line_Manufacturer.png")
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(Automobile_data["horsepower"], Automobile_data["price"])
plt.title("Horsepower vs Price")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.savefig("Scatter_Horsepower_Price.png")
plt.show()

fuel_counts = Automobile_data["fuel-type"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(fuel_counts,
        labels=fuel_counts.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Fuel Type Distribution")
plt.savefig("Pie_FuelType.png")
plt.show()

plt.figure(figsize=(7,5))
plt.boxplot(Automobile_data["price"])
plt.title("Box Plot of Car Prices")
plt.ylabel("Price")
plt.savefig("BoxPlot_Price.png")
plt.show()

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    Automobile_data["horsepower"],
    Automobile_data["engine-size"],
    Automobile_data["price"]
)

ax.set_xlabel("Horsepower")
ax.set_ylabel("Engine Size")
ax.set_zlabel("Price")
plt.title("3D Scatter Plot")
plt.savefig("3D_Scatter.png")
plt.show()

Automobile_data.to_csv("Automobile_data_cleaned.csv", index=False)
