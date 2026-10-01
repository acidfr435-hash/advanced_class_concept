import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original array: ")
print(arr)
print("\nElements from index 2 to 5: ")
print(arr[2:6])
print("\nElements from index 5 to end: ")
print(arr[5:])
print("\nEvery second element: ")
print(arr[::2])

print("Sum of all elements: ", np.sum(arr))
print("Mean of all elements: ", np.mean(arr))
print("Standard deviation of all elements: ", np.std(arr))
print("maximum element: ", np.max(arr))
print("minimum element: ", np.min(arr))

arr = arr + 4
print("\nArray after adding 4 to each element: ")
print(arr)