import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    'area': [2600, 3000, 3200, 3600, 4000, 4100],
    'bedroom': [3, 4, 4, 3, 5, 6],
    'age': [20, 15, 18, 30, 8, 8],
    'price': [550000, 565000, 610000, 595000, 760000, 810000]
})

print(df)

plt.scatter(df.area, df.price, color='red', marker='+')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

reg = LinearRegression().fit(df[['area', 'bedroom', 'age']], df.price)
print(reg.predict([[3000, 3, 40]]))09:40 26-11-2026