import numpy as np;

arr = np.arange(1,11)
print(arr)
print()

#Bracket Indexing and Selection
print(arr[7])
print(arr[3:])
print(arr[0:5])
print()

#Broadcasting
arr1 = np.arange(0,5)
print(arr1)
arr1[0:4]=100
print(arr1)
slice_of_array=arr1[0:3]
print(slice_of_array)
slice_of_array[:]=88
print(slice_of_array)
print(arr1)
print()
arr_copy=arr1.copy()
print(arr_copy)
print()


#Indexing 2D Array

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
print(arr_2d[1][0])
print(arr_2d[1,0])
print(arr_2d[:2,1:])
print(arr_2d[2,:])
print()
print()


#Fancy Indexing
arr2d = np.zeros((10,10))
print(arr2d)
arr_length = arr2d.shape[1]
print(arr_length)
for i in range(arr_length):
    arr2d[i] = i
print(arr2d)
print()
print(arr2d[[6,4,2,7]])


#Selection
arrsel = np.arange(1,11)
print(arrsel >4)
bool_arr = arrsel>5
print(arrsel[bool_arr])
