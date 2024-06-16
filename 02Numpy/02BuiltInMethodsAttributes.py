import numpy as np;

#arange method
arr1 = np.arange(0,11,2)
print(arr1)
print()

#zeros and ones
arr2 = np.zeros(5)
print(arr2)
print()
arr3 = np.ones((3,4))
print(arr3)
print()

#linespace
arr4 = np.linspace(0,10,3);
arr5 = np.linspace(0,12,5)
print(arr4)
print()
print(arr5)
print()

#eye
arr6 = np.eye(4)
print(arr6)
print()

#random
arr7 = np.random.rand(3,3)
print(arr7)
print()
arr8=np.random.randn(5,5)
print(arr8)
print()
arr9 = np.random.randint(0,10,5)
print(arr9)
print()

#Reshape
arr10 = np.arange(12)
arr11 = arr10.reshape(3,4)
print(arr11)
print()


#max,min,argmax,argmin
print(arr10.max())
print(arr10.argmax())
print(arr10.min())
print(arr10.argmin())
print()

#shape
arr12 = np.array([[1,2,3],[4,5,6],[6,6,7]])
print(arr12.shape)
print(arr12.reshape(3,3).shape)
print()

#dtype
print(arr12.dtype)


