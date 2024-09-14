def add_matrices(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

def subtract_matrices(A, B):
    result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

def multiply_matrices(A, B):
    result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    return result

def trace_matrix(A):
    return sum(A[i][i] for i in range(len(A)))

# Example usage:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

print("Addition of A and B:")
for row in add_matrices(A, B):
    print(row)

print("Subtraction of A and B:")
for row in subtract_matrices(A, B):
    print(row)

print("Multiplication of A and B:")
for row in multiply_matrices(A, B):
    print(row)

print("Trace of Matrix A:", trace_matrix(A))