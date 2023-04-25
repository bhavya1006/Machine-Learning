import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
d = {"Area(sqcm)":[2600,3027,2985,3879,4399,5409],
     "Price(rs)":[483000,529800,499000,582990,642999,730099]}

# dataframe
df = pd.DataFrame(d)

# checking null
# print(df.isnull().sum())

# appointing independent and dependent variable
x = df[["Area(sqcm)"]]
y = df["Price(rs)"]
# print(type(x))
# print(type(y))
# print(x)
# print(y)

# Applying model
m1 = LinearRegression()
m1.fit(x,y)
m1.score(x,y)
ypred = m1.predict(x)
 
# other way to get slope and intercept 
m = m1.coef_
c = m1.intercept_


#  Defining predition in dataframe
df["Prediction"] = ypred




# applying chart
plt.scatter(df["Area(sqcm)"],df["Price(rs)"],label="Actual Data")
plt.plot(df["Area(sqcm)"],df["Prediction"],label="Predicted Data",color='green')
plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.title("Area vs price --> Linear Regression")
plt.show()


from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

def get_metrics():
    mae = mean_absolute_error(y,ypred)
    mse = mean_squared_error(y,ypred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y,ypred)

    print("MAE",mae)
    print("MSE",mse)
    print("RMSE",rmse)
    print("R2 Score",r2)

get_metrics()

# for any specific area we can simply pass that (eg. 29930sqcm) in place 
# of the argument where we have passed x or df["Area(sqcm)"].



