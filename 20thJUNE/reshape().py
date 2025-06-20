import numpy as np
x=[[1,2,3],[4,5,6]]  #2 rows ,3 columns
a=np.array(x)
m=np.matrix(x)   
a1=a.reshape(3,2)
print(a1)
m1=m.reshape(3,2)
print(m1)
