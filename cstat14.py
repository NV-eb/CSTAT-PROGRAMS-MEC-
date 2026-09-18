import numpy as np

# Create a 3D array
arr = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]
])

# Extract diagonal from each 2D layer
diagonals = np.diagonal(arr, axis1=1, axis2=2)

print("3D Array:")
print(arr)

print("\n2D Diagonals:")
print(diagonals) 
