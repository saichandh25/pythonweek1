import numpy as np
"generates 20 random float numbers from 1 to 20"
x = np.random.uniform(1,high=20, size=20)
"reshaped the array to (4,5) matrix form and round the decimal values"
a = x.reshape(4, 5).round(2)
print(a)
"retrives the max valuve from each row"
row_maxs = np.max(a, axis=1)
print(row_maxs)
"converts the max value in each row to zero"
b = np.where(a==row_maxs.reshape(-1,1),0,a)
print(b)

