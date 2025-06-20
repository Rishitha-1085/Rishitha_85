#unique elements
import numpy as np
a=np.array([[1,1,1],[2,2,2],[3,3,3]])
m=np.matrix('1,1,1;2,2,2;3,3,3')
print(a)
print(m)
print(np.unique(a))  #o/p 1,2,3
print(np.unique(m))
