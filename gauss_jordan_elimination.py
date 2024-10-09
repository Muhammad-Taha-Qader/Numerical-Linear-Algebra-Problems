import numpy as np

# Augmented matrix for the system of equations
A = np.array([
    [9, 0, -3, 0, 0, 120],
    [4, -4, 0, 0, 0, 0],
    [0, -2, 9, 0, 0, 350],
    [0, 1, 6, -9, 2, 0],
    [5, 1, 0, 0, -6, 0]
], dtype=float)

def gauss_jordan_elimination(A):
    n = len(A)

    for i in range(n):
        # Make the diagonal element 1
        A[i] = A[i] / A[i][i]
        
        # Make the other elements in the column 0
        for j in range(n):
            if i != j:
                A[j] = A[j] - A[j][i] * A[i]

    return A

# Apply Gauss-Jordan elimination
result = gauss_jordan_elimination(A)

# Extract the solutions from the result
solution = result[:, -1]

print("The solution for the system is:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
print("x4 =", solution[3])
print("x5 =", solution[4])
