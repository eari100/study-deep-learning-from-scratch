import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

# elementwise
B = np.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)

# broadcast
print(A * 10)