import numpy as np

arr_10 = np.array([[1,2],[3,4],[1,2],[3,4]])
#print(np.shape(arr_10))
#print(np.size(arr_10))
#print(np.ndim(arr_10))

arr2=np.arange(10)
print(arr2)

arr3=np.arange(0,10,2)
print(arr3)

print(arr[:])


arr=np.array([1,2,3,4,5,6,7])
y=arr>3
print(arr>3)
print(y)
arr>3
print(arr)
x= arr[arr>3]
print(x)

print(arr[-1:-7])
print(arr[-7:])


arr1 = np.array([[1,2,3],[4,5,6]])
arr1_flat=arr1.flatten()
print(arr1_flat)

print(arr1.T)