# Read the size of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Dictionary to store non-zero elements
sparse = {}

print("Enter the matrix elements:")
for i in range(rows):
    for j in range(cols):
        value = int(input(f"Element [{i}][{j}]: "))
        if value != 0:
            sparse[(i, j)] = value

# Display the dictionary
print("\nSparse Matrix (Dictionary Representation):")
print(sparse)

# Display the original matrix
print("\nMatrix:")
for i in range(rows):
    for j in range(cols):
        print(sparse.get((i, j), 0), end=" ")
    print()
