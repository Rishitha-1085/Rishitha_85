import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]] #list
a=np.array(x)    #list data converted to array
print(a)
print(a.dtype)
print(a.shape)
print(a.ndim) #specifies no.of dimensions
print(a.size) #size of array
print(*a)    #remover