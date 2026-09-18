import numpy as np

# Define two arrays
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [0, 5],
    [6, 7]
])

# Calculate Kronecker product
result = np.kron(A, B)

print("Array A:")
print(A)

print("\nArray B:")
print(B)

print("\nKronecker Product:")
print(result)
