import numpy as np
A = np.array([[3., -0.1, -0.2, 7.85],
            [0.1, 7., -0.3, -19.3],
            [0.3, -0.2, 10, 71.4]])
#PIVOT A[0,0]
m = A[1, 0]/A[0, 0]
for j in range(0, 4):
 A[1, j] = A[1, j] - m*A[0, j]
m = A[2, 0]/A[0, 0]
for j in range(0, 4):
 A[2, j] = A[2, j] - m*A[0, j]
print(A)