import numpy as np
n=int(input())
a=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    x=int(input())
    a[i]=x
print(a)
a.sort()
print(a)
