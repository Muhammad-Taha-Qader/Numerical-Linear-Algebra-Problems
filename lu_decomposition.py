import numpy as np

def lu_decomposition_manual(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        # Upper Triangular Matrix U
        for k in range(i, n):
            sum_U = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_U

        # Lower Triangular Matrix L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Diagonal as 1 for L
            else:
                sum_L = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_L) / U[i][i]
    
    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros_like(b, dtype=np.double)
    
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros_like(y, dtype=np.double)
    
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i][i]
    
    return x

# Coefficient matrix A
A = np.array([
    [8, 2, 2, 5, 6],
    [0, 1, 1, 2, 2],
    [8, 6, 3, 1, 3],
    [2, 8, 4, 9, 0],
    [1, 7, 8, 4, 8]
], dtype=float)

# Right-hand side vector b
b = np.array([8, 4, 3, 7, 7], dtype=float)

# Perform LU decomposition manually
L, U = lu_decomposition_manual(A)

print("Lower triangular matrix L:")
print(L)
print("Upper triangular matrix U:")
print(U)

# Step 1: Solve Ly = b using forward substitution
y = forward_substitution(L, b)

# Step 2: Solve Ux = y using backward substitution
x = backward_substitution(U, y)

print("\nSolution for the system:")
print(x)
