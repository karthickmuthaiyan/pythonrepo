import numpy as np
arr=np.zeros(8)
arr3d=arr.reshape((2,2,2))
print(arr3d)
arr=arr3d.ravel()
print(arr)
