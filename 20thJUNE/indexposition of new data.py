#Finding the index position of new data
import numpy as np
n=int(input())
a=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    x=int(input())
    a[i]=x
print(a)

d=int(input())
ans=np.searchsorted(a,d)
print(ans)
print(a)