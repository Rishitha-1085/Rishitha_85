import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,0],[0,1],[1,0]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('1,0;0,1;1,0')
#Matrix multiplication
print(c*d)

ans=c.dot(d)
print(ans)
#array multiplication
ans1=a.dot(b)
print(ans1)