#two dimension array operation
import numpy as np
r,c=map(int,input().split())
m=np.ndarray(shape=(r,c),dtype=int)

for i in range(r):
    for j in range(c):
        d=int(input())
        m[i][j]=d
        
for i in range(r):
    for j in range(c):
        print(m[i][j],(i,j),end=" ")
    print()