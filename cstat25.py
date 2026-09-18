import numpy as np

X = np.array([10, 20, 30, 40, 50])
Y = np.array([15, 25, 35, 45, 55])

correlation = np.corrcoef(X, Y)

print("X:", X)
print("Y:", Y)

print("\nCorrelation Matrix:")
print(correlation)

print("\nPearson Correlation Coefficient:")
print(correlation[0, 1])
