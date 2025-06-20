# MEAN FUNCTION 

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
ans=a.mean()
ans1=m.mean()
print(ans)   #45/9=5
print(ans1