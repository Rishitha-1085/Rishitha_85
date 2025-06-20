'''
CONSTANT ADDITION
'''
import numpy 
a=numpy.array([[1,2,3],[4,5,6]])
b=numpy.array([[4,5,6],[1,2,3]])
a=a+1   #constant addition-1 is added to every element of array
print(a)
b=b-1
print(b)
a=a*2
print(a)
a=a/2
print(a)
a%=2 #not executed
print(a)
a**=2
print(a)
a//=2
print(a)
