import matplotlib.pyplot as plt
import pandas as pd             #import the required modules
df = pd.read_csv('train.csv')  # import the datasets
y = df['SalePrice']
x = df['GarageArea']
print('original shape of datashape', df.shape)
#scatter plot with outliers
plt.scatter(x, y)
plt.title("original dataframe")
plt.ylabel("SalesPrice")
plt.xlabel("GarageArea")
plt.show()
#using inter quartile range removing outlyers and ploting scatter plot
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
modified_data = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
y = modified_data['SalePrice']
x = modified_data['GarageArea']
print('after removing outliers inter', modified_data.shape)
plt.scatter(x, y)
plt.title("after deleting outliers")
plt.ylabel("SalesPrice")
plt.xlabel("GarageArea")
plt.show()

