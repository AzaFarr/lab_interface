def gauss_elimination(A, b):

    n = len(b)

    for i in range(n):

        for k in range(i + 1, n):
            m = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= m * A[i][j]
            b[k] -= m * b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x





