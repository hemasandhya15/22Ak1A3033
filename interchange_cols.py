def interchange_columns(matrix):
    return [row[-1:] + row[:-1] for row in matrix]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original Matrix:")
for row in matrix:
    print(row)

interchanged_matrix = interchange_columns(matrix)
print("Interchanged Matrix:")
for row in interchanged_matrix:
    print(row)