import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]] #
a=np.array(x) 
for i in range(3):
    for j in range(3):
        print(a[i][j],(i,j),end=' ')
    print()