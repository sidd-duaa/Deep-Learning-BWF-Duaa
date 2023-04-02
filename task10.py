import numpy as np

a = np.array([1,2,3])
print(a)
b = np.array([[9.0, 8.0, 7.0],[6.0, 5.0, 4.0]])
print(b)

print(b.ndim) #Dimensions
print(b.shape) #Shape
print(a.dtype) #Type - By default int32

c = np.array([3,4,2,1], dtype='int16') #Changing dtype
print(c.dtype)

print(c.itemsize) #No of bytes
print(c.size) #No of elements
print(c.nbytes) #Total bytes
print(c.itemsize * c.size)

# Indexing and Slicing
d = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(d[1,-2])
print(d[0, :])
print(d[:, -2])
print(d[0,1:-1:2])
d[1,5] = 20
print(d)
d[:,2] = [5,6]
print(d)

# 3 Dimensional
e = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(e)
print(e[0,1,1])
# print(e[:,1,:])
e[:,1,:] = [[9,9],[8,8]]
print(e)

# Different Types of Arrays
print(np.zeros((2,3)))
print(np.ones((2,3),dtype='int32'))
print(np.full((2,3),4))
print(np.full_like(a, 4))
print(np.random.rand(2,3))
print(np.random.random_sample(a.shape))
print(np.random.randint(5,size=(3,2)))
print(np.identity(3))

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

# Creating [[1,1,1,1,1],[1,0,0,0,1],[1,0,9,0,1],[1,0,0,0,1],[1,1,1,1,1]]
challenge = np.ones((5,5))
challenge[1:4,1:4] = 0
challenge[2,2] = 9
print(challenge)

# Copying
a = np.array([1,2,3,4])
b = a.copy()
b[0] = 6
print(b)
print(a)

# Arithmetic Operations
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(np.sin(a))
print(np.cos(a))

b = np.array([[[1,3],[5,7]],[[9,11],[13,15]]])
c = np.array([[[2,4],[6,8]],[[10,12],[14,16]]])
print(b+c)
print(b-c)
print(b*c)
print(b/c)