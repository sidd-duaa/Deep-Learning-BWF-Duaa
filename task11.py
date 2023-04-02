import numpy as np

'''# Linear Algebra

a = np.array([[4,-3,1],[2,1,3],[-1,2,-5]])
b = np.array([-10,0,17])
print(a)
print(b)

print(np.matmul(a,b)) # Multiplying
print(np.linalg.solve(a,b)) # Solution
print(np.linalg.det(a)) # Determinant
print(np.hstack((a, b.reshape(3,1)))) # Unifying

# Statistics

stats = np.array([[1,2,3],[4,5,6]])

print(np.min(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))

print(np.max(stats))
print(np.max(stats, axis=0))
print(np.max(stats, axis=1))

print(np.sum(stats))
print(np.sum(stats, axis=0))

x = np.array([1,2,4,6,4,6,3,6,2,4,2,1])
print(np.mean(x))
print(np.median(x))

from scipy import stats

print(stats.mode(x))

print(np.std(x))'''

array = np.array([1,2,3,6,7,8,10,11,12,15,16,17])
print(np.quantile(array, 0.10))
print(np.quantile(array, 0.5))
print(np.quantile(array, 0.95))