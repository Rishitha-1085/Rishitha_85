# sum,max,min,len,prod,transpose,trace functions

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a)
print(m)
'''print(sum(a)) #columns sum sum(a)-used in 1D array'''
"""Sum function"""
print(a.sum())  #45
print(m,sum())   #output:45
print(a.sum(axis=1)) #row wise sum operation
print(m.sum(axis=1))
print(a.sum(axis=0)) #column wise sum operation
print(m.sum(axis=0))
print(a.cumsum())   #adding step by step elements data-cummulative sum
print(m.cumsum())
'''MAX FUNCTION'''
print(a.max())
print(m.max())
print(a.max(axis=1))    #row wise maximum value
print(m.max(axis=1))
print(a.max(axis=0))   #column wise maximum value
print(m.max(axis=0))
''' MIN FUNCTION'''
print(a.min())
print(m.min())
print(a.min(axis=1))    #row wise minimum value
print(m.min(axis=1))
print(a.min(axis=0))   #column wise min value
print(m.min(axis=0))
'''len Function'''
print(a.size())
print(m.size())
'''Prod Function'''
print(a.prod())
print(m.prod())
print(a.prod(axis=1))
print(m.prod(axis=1))
print(a.prod(axis=0))
print(m.prod(axis=0))
'''Transpose(T)-Interchange of rows and columns data'''
print(a.T)
print(m.T)
'''OR use func transpose '''
print(a.transpose())
print(m.transpose())

#sum of DIagonal Elements
print(a.trace())
print(m.trace())