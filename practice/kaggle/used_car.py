import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns


def cat_plot():
    fig, axes = plt.subplots(3, 2, figsize=(18, 18))
    fig.suptitle("Bar plot for all categorical variables in the dataset")
    sns.countplot(
        ax=axes[0, 0],
        x="Fuel_Type",
        data=car_data,
        color="blue",
        order=car_data["Fuel_Type"].value_counts().index,
        stat="percent",
    )
    sns.countplot(
        ax=axes[0, 1],
        x="Transmission",
        data=car_data,
        color="blue",
        order=car_data["Transmission"].value_counts().index,
        stat="percent",
    )
    sns.countplot(
        ax=axes[1, 0],
        x="Owner_Type",
        data=car_data,
        color="blue",
        order=car_data["Owner_Type"].value_counts().index,
        stat="percent",
    )
    sns.countplot(
        ax=axes[1, 1],
        x="Location",
        data=car_data,
        color="blue",
        order=car_data["Location"].value_counts().index,
    )
    sns.countplot(
        ax=axes[2, 0],
        x="Brand",
        data=car_data,
        color="blue",
        order=car_data["Brand"].head(20).value_counts().index,
        stat="percent",
    )
    sns.countplot(
        ax=axes[2, 1],
        x="Model",
        data=car_data,
        color="blue",
        order=car_data["Model"].head(20).value_counts().index,
    )
    axes[1][1].tick_params(labelrotation=45)
    axes[2][0].tick_params(labelrotation=90)
    axes[2][1].tick_params(labelrotation=90)
    plt.show()


def num_plot():
    for col in num_cols:
        print("Skew : ", col, round(car_data[col].skew(), 2))

        plt.figure(figsize=(15, 4))
        plt.subplot(1, 2, 1)
        car_data[col].hist(grid=False)
        plt.ylabel("Count")
        plt.subplot(1, 2, 2)
        sns.boxplot(x=car_data[col])
        plt.show()


car_data = pd.read_csv("used_cars_data.csv")
# print(car_data.info())
# print(car_data['Engine'])
# print(car_data.describe())
# print(car_data.shape)
# print(car_data.duplicated())
# print(car_data.nunique())
# print(((car_data.isnull().sum()) / (len(car_data)) * 100))
# print(len(car_data))


car_data.drop(["S.No."], axis=1, inplace=True)
car_data["car_age"] = date.today().year - car_data["Year"]
# print(car_data.head())
car_data["Brand"] = car_data.Name.str.split().str.get(0)
car_data["Model"] = car_data.Name.str.split().str.get(
    1
) + car_data.Name.str.split().str.get(2)
# print(car_data.head())
# print(car_data.Brand.unique())
srchfor = ["Land", "Isuzu", "ISUZU", "Mini"]

# print(car_data[car_data.Brand.str.contains("|".join(srchfor), na=False)])
# car_data["Brand"].replace({"ISUZU": "Isuzu", "Mini": "Mini Cooper", "Land": "Land Rover"}, inplace=True)
# print(car_data.head())
# print(car_data[car_data.Brand.str.contains("|".join(srchfor), na=False)])
car_data.replace(
    {"Brand": {"ISUZU": "Isuzu", "Mini": "Mini Cooper", "Land": "Land Rover"}},
    inplace=True,
)
# print(car_data[car_data.Brand.str.contains("|".join(srchfor), na=False)])

# print(car_data.describe(include='all').T)
# print(car_data.select_dtypes(include=["float64"]).nunique())
# print(car_data.info())

cat_cols = car_data.select_dtypes(include=["object"]).columns
print(cat_cols)
num_cols = car_data.select_dtypes(include=np.number).columns.tolist()
print(num_cols)
# print(car_data['Price'].skew())

# num_plot()
# cat_plot()
# print(car_data["Fuel_Type"].value_counts().index)


# Function for log transformation of the column
def log_transform(data, col):
    for colname in col:
        if (data[colname] == 1.0).all():
            data[colname + "_log"] = np.log(data[colname] + 1)
        else:
            data[colname + "_log"] = np.log(data[colname])
    # print(data["Kilometers_Driven_log"])
    # print(data["Kilometers_Driven"])


log_transform(car_data, ["Kilometers_Driven", "Price"])
# sns.displot(data=car_data, x="Price_log", kde=True)
# sns.displot(data=car_data, x="Kilometers_Driven_log", kde=True)
# plt.figure(figsize=(13, 17))
# sns.pairplot(data=car_data.drop(["Kilometers_Driven", "Price"], axis=1))
# plt.show()

# print(car_data)
# print(car_data.groupby("Location")["Price_log"].mean().sort_values(ascending=False))
# fig, axarr = plt.subplots(4, 2, figsize=(12, 18))
# car_data.groupby("Location")["Price_log"].mean().sort_values(ascending=False).plot.bar(
#     ax=axarr[0][0], fontsize=12
# )
# axarr[0][0].set_title("Location Vs Price", fontsize=18)
# car_data.groupby("Transmission")["Price_log"].mean().sort_values(
#     ascending=False
# ).plot.bar(ax=axarr[0][1], fontsize=12)
# axarr[0][1].set_title("Transmission Vs Price", fontsize=18)
# car_data.groupby("Fuel_Type")["Price_log"].mean().sort_values(ascending=False).plot.bar(
#     ax=axarr[1][0], fontsize=12
# )
# axarr[1][0].set_title("Fuel_Type Vs Price", fontsize=18)
# car_data.groupby("Owner_Type")["Price_log"].mean().sort_values(
#     ascending=False
# ).plot.bar(ax=axarr[1][1], fontsize=12)
# axarr[1][1].set_title("Owner_Type Vs Price", fontsize=18)
# car_data.groupby("Brand")["Price_log"].mean().sort_values(ascending=False).head(
#     10
# ).plot.bar(ax=axarr[2][0], fontsize=12)
# axarr[2][0].set_title("Brand Vs Price", fontsize=18)
# car_data.groupby("Model")["Price_log"].mean().sort_values(ascending=False).head(
#     10
# ).plot.bar(ax=axarr[2][1], fontsize=12)
# axarr[2][1].set_title("Model Vs Price", fontsize=18)
# car_data.groupby("Seats")["Price_log"].mean().sort_values(ascending=False).plot.bar(
#     ax=axarr[3][0], fontsize=12
# )
# axarr[3][0].set_title("Seats Vs Price", fontsize=18)
# car_data.groupby("car_age")["Price_log"].mean().sort_values(ascending=False).plot.bar(
#     ax=axarr[3][1], fontsize=12
# )
# axarr[3][1].set_title("car age Vs Price", fontsize=18)
# plt.subplots_adjust(hspace=1.0)
# plt.subplots_adjust(wspace=0.5)
# sns.despine()
# plt.show()

print(car_data.info())
# car_data.loc[car_data["Mileage"] == 0.0, "Mileage"] = np.nan

car_data["Mileage"].fillna(value="0.0 kmpl", inplace=True)

# print(df_filter)
car_data["Seats"].fillna(value=np.mean(car_data['Seats']), inplace=True)
print(car_data.info())

# plt.figure(figsize=(12, 7))
# new_num_cols = num_cols + ["Kilometers_Driven_log", "Price_log"]
# num_car_data = car_data[new_num_cols]
# sns.heatmap(
#     num_car_data.drop(["Kilometers_Driven", "Price"], axis=1).corr(),
#     annot=True,
#     vmin=-1,
#     vmax=1,
# )
# plt.show()
