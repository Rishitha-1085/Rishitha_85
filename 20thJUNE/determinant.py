# to find determinant of matrix:
import numpy as np
a=np.array([[6,1,1],[4,-2,5],[2,8,7]])
m=np.matrix('6,1,1;4,-2,5;2,8,7')
print(a)
print(m)
print(np.linalg.det(a))
print(np.linalg.det(m))

