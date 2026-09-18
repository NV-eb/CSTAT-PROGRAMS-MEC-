import numpy as np

# Define a square matrix
A = np.array([
    [1, 2],
    [3, 4]
])

print("Original Matrix:")
print(A)

# Find inverse
inverse = np.linalg.inv(A)

print("\nInverse Matrix:")
print(inverse)
