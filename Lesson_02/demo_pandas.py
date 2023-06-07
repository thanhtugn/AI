import pandas as pd
import numpy as np

# arr = np.array([1, 2, 3, 4], dtype=int)
# print(arr)

# arr1 = np.array([1, 6, 8, 4, 9])
# print(arr1)

# arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2)

# arr3 = np.zeros([1,2], dtype=int)
# print(arr3)

# arr4 = np.ones([1,2,3], dtype=int)
# print(arr4)

# arr5 = np.ones([2,3,4], dtype=int)
# print(arr5)

# arr6 = np.arange(1,17,2) 
# print(arr6)

# arr7 = np.full((2,3),5)
# print(arr7)

# arr8 = np.full((3,5),3)
# print(arr8)

# arr9 = np.random.random((2,3))
# print(arr9)


#---------------------

rdn = np.loadtxt("random_array.txt", dtype=int, delimiter= ',')
print (rdn)