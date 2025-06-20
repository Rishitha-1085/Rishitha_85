import numpy as np
a=np.array([[12,4,6],[3,16,9],[9,8,12]])
m=np.matrix('12,4,6;3,16,9;9,8,12')
x=np.sort(a,axis=None)
print(x)
y=np.sort(m,axis=None)
print(y)
x=np.sort(a,axis=1)  #rowdata sort
print(x)
y=np.sort(m,axis=1)
print(y)
x=np.sort(a,axis=0)  #columnwise sort
print(x)
y=np.sort(m,axis=0)
print(y)
#Reverse-decending order of elements 
x=np.sort(a,axis=None)[::-1]
print(x)
y=np.sort(m,axis=None)[::-1]  #not executed
print(y)
x=(np.sort(-a,axis=1))*-1
print(x)
y=(np.sort(-a,axis=0))*-1
print(y)
#not executed
x=(np.sort(-m,axis=1))*-1
print(x)
y=(np.sort(-m,axis=0))*-1
print(y)