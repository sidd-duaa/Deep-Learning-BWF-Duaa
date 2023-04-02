import numpy as np

# Broadcasting

var1 = np.array([1,2,3])
var2 = np.array([[1],[2],[3]])
print(var1 + var2) 

a = np.array([[1],[2]])
b = np.array([[1,2,3],[1,2,3]])
print(a.shape)
print(b.shape)
print(a+b)