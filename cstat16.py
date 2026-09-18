import numpy as np

n = int(input("Enter the number of terms: "))

phi = (1 + np.sqrt(5)) / 2

print("Fibonacci Series:")

for i in range(n):
    fib = (phi ** i - (1 - phi) ** i) / np.sqrt(5)
    print(round(fib), end=" ")
