#Question 3 part b

import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iterations=100):
    """
    Solves the linear system Ax = b using the Jacobi iterative method.

    Parameters:
    A (ndarray): Coefficient matrix.
    b (ndarray): Right-hand side vector.
    x0 (ndarray): Initial guess for the solution.
    tol (float): Tolerance for convergence.
    max_iterations (int): Maximum number of iterations.

    Returns:
    x (ndarray): Approximated solution vector.
    iterations (int): Number of iterations performed.
    """
    n = A.shape[0]
    x = x0.copy()
    x_new = np.zeros_like(x0)

    # Precompute the inverse of the diagonal elements
    D = np.diag(A)
    if np.any(D == 0):
        raise ValueError("Matrix A has zero(s) on its diagonal, Jacobi method cannot proceed.")

    for iteration in range(1, max_iterations + 1):
        for i in range(n):
            # Sum over all j != i
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        # Compute the difference for convergence
        diff = np.linalg.norm(x_new - x, ord=np.inf)
        print(f"Iteration {iteration}: {x_new}")

        if diff < tol:
            print(f"Converged in {iteration} iterations.")
            return x_new, iteration

        x = x_new.copy()

    print("Jacobi method did not converge within the maximum number of iterations.")
    return x, iteration

# Define the coefficient matrix A
A = np.array([
    [10, -1,  2,  0],
    [-1, 11, -1,  3],
    [ 2, -1, 10, -1],
    [ 0,  3, -1,  8]
], dtype=float)

# Define the right-hand side vector b
b = np.array([6, 25, -11, 15], dtype=float)

# Initial guess x0 = (0, 0, 0, 0)^T
x0 = np.zeros(4)

# Perform Jacobi iteration
solution, iterations = jacobi(A, b, x0)

print("\nApproximate solution after Jacobi iterations:")
print(solution)

