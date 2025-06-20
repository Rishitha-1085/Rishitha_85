import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]] 
m=np.matrix(x)
m+=1
print(m)
m*=2
print(m)
m-=1
print(m)
m=m/2
print(m)
m%=2
print(m)
m**=2  #exponential operation does not work in matrix
print(m)
m//=2
print(m)