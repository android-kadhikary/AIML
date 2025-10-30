import numpy as np

# arr_10 = np.array([[1,2],[3,4],[1,2],[3,4]])
# #print(np.shape(arr_10))
# #print(np.size(arr_10))
# #print(np.ndim(arr_10))

# arr2=np.arange(10)
# print(arr2)

# arr3=np.arange(0,10,2)
# print(arr3)

# print(arr[:])


# arr=np.array([1,2,3,4,5,6,7])
# y=arr>3
# print(arr>3)
# print(y)
# arr>3
# print(arr)
# x= arr[arr>3]
# print(x)

# print(arr[-1:-7])
# print(arr[-7:])


# arr1 = np.array([[1,2,3],[4,5,6]])
# arr1_flat=arr1.flatten()
# print(arr1_flat)

# print(arr1.T)

arr=np.array([2,3,4])
ex=np.expand_dims(arr,axis=1)
print(ex)


arr1d=np.array([2,3,4,12,13,14,11,22])
arr2d=arr1d.reshape(2,4)
print(f"Reshaped to 2D array: {arr2d}, shape: {arr2d.shape}")

print(arr2d.reshape(8))
print(arr2d.reshape(4,2))
arr3d=arr2d.reshape(2,2,2)
print(arr3d)
print("reshape with -1 in first dim",arr3d.reshape(-1,2))
print("reshape with -1 in first and 2nd dim",arr3d.reshape(-1,2))
print("flatten with reshape",arr3d.reshape(-1))
print("flatten",arr3d.flatten())