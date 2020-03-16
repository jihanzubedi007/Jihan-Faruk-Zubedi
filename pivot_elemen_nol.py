import numpy as np
A = np.array([[3., -0.1, -0.2, 7.85],
            [0.1, 7., -0.3, -19.3],
            [0.3, -0.2, 10, 71.4]])
# PIVOT A[0,0]
for i in range(1, 3):
 m = A[i, 0]/A[0, 0]
 for j in range(0, 4):
    A[i, j] = A[i, j] - m*A[0, j]
# PIVOT A[1,1]
for i in range(2, 3):
 m = A[i, 1]/A[1, 1]
 for j in range(0, 4):
    A[i, j] = A[i, j] - m*A[1, j]
print(A)