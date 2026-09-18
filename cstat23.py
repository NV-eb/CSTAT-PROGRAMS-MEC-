import numpy as np

arr = np.array([1, 3, 6, 10, 15, 21])

n = int(input("Enter the order of difference: "))

result = np.diff(arr, n=n)

print("Original Array:")
print(arr)

print("\n", n, "th Order Difference:")
print(result)
