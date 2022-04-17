import numpy as np


A = np.array([1, 2, 3, 4])
print(A)
# 차원 수
print(np.ndim(A))
# 배열의 형상을 튜플로 반환
print(A.shape)
print(A.shape[0])

B = np.array([[1,2], [3,4], [5,6]])
print(B)
print(np.ndim(B))
print(B.shape)