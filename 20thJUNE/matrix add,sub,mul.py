#MATRIX ADDITION ,SUB,MULTIPLICATION
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,6],[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
#Addition 
ans=np.sum([a,b],axis=None)
print(ans)
ans1=np.sum([a,b],axis=1)
print(ans1)
ans2=np.sum([a,b],axis=0)
print(ans2)

print(a+b)

#Matrix Addition
ans=np.sum([c,d],axis=None)
print(ans)
ans1=np.sum([c,d],axis=1)
print(ans1)
ans2=np.sum([c,d],axis=0)
print(ans2)
#Matrix Difference
print(c-d)
