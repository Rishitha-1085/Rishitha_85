import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]] 
a=np.array(x)
m=np.matrix(x)   
ans=a.flatten()         #convert the multiDimension array data to 1D data   
print(ans)
ans1=m.flatten()
print(ans1)     #nestedlist is printed
