import numpy as np
x = np.random.uniform(1,high=20, size=20)
a = x.reshape(4, 5).round(2)
print(a)
print("\n")

row_maxs = np.max(a, axis=1)
print(row_maxs)
print("\n")
print(row_maxs.reshape(-1,1))
print("\n")
b = np.where(a==row_maxs.reshape(-1,1),0,a)
print(b)

