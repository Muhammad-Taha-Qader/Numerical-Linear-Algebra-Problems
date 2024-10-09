import numpy as np

# Augmented matrix for the system of equations
A = np.array([
    [9, 2, 0, 0, 90],
    [0, 3, 4, 0, 0],
    [0, 5, -1, 1, 25],
    [-2, 0, 4, 0, 0]
], dtype=float)

def gauss_elimination(A):
    n = len(A)

    # Forward elimination to create an upper triangular matrix
    for i in range(n):
        # Make the diagonal element 1
        A[i] = A[i] / A[i][i]
        
        # Eliminate the values below the pivot (i.e., below diagonal elements)
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]

    # Back substitution to solve for variables
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = A[i][-1] - np.dot(A[i][i+1:n], x[i+1:n])

    return x

# Apply Gauss Elimination
solution = gauss_elimination(A)

print("The solution for the system is:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
print("x4 =", solution[3])
