import numpy as np

# Define two vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Inner product
inner = np.inner(A, B)

# Outer product
outer = np.outer(A, B)

# Cross product
cross = np.cross(A, B)

print("Vector A:", A)
print("Vector B:", B)

print("\nInner Product:")
print(inner)

print("\nOuter Product:")
print(outer)

print("\nCross Product:")
print(cross)
