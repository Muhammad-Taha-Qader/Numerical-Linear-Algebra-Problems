"Numerical Linear Algebra Problems". These questions focus on solving systems of linear equations using various numerical methods, such as:

- Gauss-Jordan Method
- Gauss Elimination Method
- Jacobi Iteration Method
- LU Decomposition Method
- Gauss-Seidel Iteration Method

Emphasizing both theoretical and computational aspects of numerical linear algebra.


## 1. Gauss-Jordan Method 
Ans was:
```bash
    taha@taha-Latitude-7490:/mnt/26B400DDB400B17B/ITU/Semester 07/Numerical Computing/Numerical Computing - MT433/Assignments/Assi 2/Numerical Linear Algebra Problems$ python3 gauss_jordan_elimination.py 
    The solution for the system is:
    x1 = 28.4
    x2 = 28.4
    x3 = 45.199999999999996
    x4 = 39.599999999999994
    x5 = 28.399999999999995
```

## 2. Gauss Elimination Method
Ans was:
```bash
    taha@taha-Latitude-7490:/mnt/26B400DDB400B17B/ITU/Semester 07/Numerical Computing/Numerical Computing - MT433/Assignments/Assi 2/Numerical Linear Algebra Problems$ python3 gauss_elimination.py
    The solution for the system is:
    x1 = 11.73913043478261
    x2 = -7.82608695652174
    x3 = 5.8695652173913055
    x4 = 70.00000000000001
```

## 3. Jacobi Iteration Method
Ans was:

```bash
    taha@taha-Latitude-7490:/mnt/26B400DDB400B17B/ITU/Semester 07/Numerical Computing/Numerical Computing - MT433/Assignments/Assi 2/Numerical Linear Algebra Problems$ python3 jacobi_iteration.py 
    Iteration 1: [ 0.6         2.27272727 -1.1         1.875     ]
    Iteration 2: [ 1.04727273  1.71590909 -0.80522727  0.88522727]
    Iteration 3: [ 0.93263636  2.05330579 -1.04934091  1.13088068]
    Iteration 4: [ 1.01519876  1.95369576 -0.96810863  0.97384272]
    Iteration 5: [ 0.9889913   2.01141473 -1.0102859   1.02135051]
    Iteration 6: [ 1.00319865  1.99224126 -0.99452174  0.99443374]
    Iteration 7: [ 0.99812847  2.00230688 -1.00197223  1.00359431]
    Iteration 8: [ 1.00062513  1.9986703  -0.99903558  0.99888839]
    Iteration 9: [ 0.99967415  2.00044767 -1.00036916  1.00061919]
    Iteration 10: [ 1.0001186   1.99976795 -0.99982814  0.99978598]
    Iteration 11: [ 0.99994242  2.00008477 -1.00006833  1.0001085 ]
    Iteration 12: [ 1.00002214  1.99995896 -0.99996916  0.99995967]
    Iteration 13: [ 0.99998973  2.00001582 -1.00001257  1.00001924]
    Iteration 14: [ 1.00000409  1.99999268 -0.99999444  0.9999925 ]
    Iteration 15: [ 0.99999816  2.00000292 -1.0000023   1.00000344]
    Iteration 16: [ 1.00000075  1.99999868 -0.99999899  0.99999862]
    Iteration 17: [ 0.99999967  2.00000054 -1.00000042  1.00000062]
    Iteration 18: [ 1.00000014  1.99999976 -0.99999982  0.99999975]
    Converged in 18 iterations.

    Approximate solution after Jacobi iterations:
    [ 1.00000014  1.99999976 -0.99999982  0.99999975]
```

## 4. LU Decomposition Method
Ans was:

```bash
    taha@taha-Latitude-7490:/mnt/26B400DDB400B17B/ITU/Semester 07/Numerical Computing/Numerical Computing - MT433/Assignments/Assi 2/Numerical Linear Algebra Problems$ python3 lu_decomposition.py 
    Solution for the system:
    [-0.0920858   0.71264793 -1.10539941  0.65606509  1.04031065]
    taha@taha-Latitude-7490:/mnt/26B400DDB400B17B/ITU/Semester 07/Numerical Computing/Numerical Computing - MT433/Assignments/Assi 2/Numerical Linear Algebra Problems$ python3 lu_decomposition.py 
    Lower triangular matrix L:
    [[ 1.          0.          0.          0.          0.        ]
    [ 0.          1.          0.          0.          0.        ]
    [ 1.          4.          1.          0.          0.        ]
    [ 0.25        7.5         1.33333333  1.          0.        ]
    [ 0.125       6.75       -0.33333333 -1.61428571  1.        ]]
    Upper triangular matrix U:
    [[  8.           2.           2.           5.           6.        ]
    [  0.           1.           1.           2.           2.        ]
    [  0.           0.          -3.         -12.         -11.        ]
    [  0.           0.           0.           8.75        -1.83333333]
    [  0.           0.           0.           0.         -12.87619048]]

    Solution for the system:
    [-0.53957101  1.43676036 -2.47300296  0.71967456  1.79844675]
```

## 5. Gauss-Seidel Iteration Method
Ans was:

```bash
```