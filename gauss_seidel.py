import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iterations=100):
    n = len(b)
    x = x0.copy()

    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            # Calculate the new value for x[i]
            sum_1 = np.dot(A[i, :i], x_new[:i])  # Use the new values from the current iteration
            sum_2 = np.dot(A[i, i+1:], x[i+1:])  # Use the old values from the previous iteration
            x_new[i] = (b[i] - sum_1 - sum_2) / A[i, i]

        # Check for convergence
        diff = np.linalg.norm(x_new - x, ord=np.inf)
        print(f"Iteration {iteration + 1}: {x_new}")

        if diff < tol:
            print(f"Converged in {iteration + 1} iterations.")
            return x_new

        x = x_new.copy()

    print("Gauss-Seidel method did not converge within the maximum number of iterations.")
    return x

# Coefficient matrix A
A = np.array([
    [12, 3, -5],
    [1, 5, 3],
    [3, 7, 13]
], dtype=float)

# Right-hand side vector b
b = np.array([1, 28, 76], dtype=float)

# Initial guess x0 = (1, 0, 1)
x0 = np.array([1.0, 0.0, 1.0], dtype=float)

# Perform Gauss-Seidel iteration
solution = gauss_seidel(A, b, x0)

print("\nApproximate solution after Gauss-Seidel iterations:")
print(solution)
