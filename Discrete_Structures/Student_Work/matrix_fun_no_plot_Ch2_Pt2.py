matrix_A = [
    [1, 0, -1, 0, 0],
    [0, 1, 0, -1, 0],
    [0, 0, 1, 0, -1],
    [-1, 0, 0, 1, 0]
]
matrix_B = [
    [0.5, 0.1, 0.3, 0.2],
    [0.2, 0.4, 0.1, 0.3],
    [0.3, 0.2, 0.4, 0.1],
    [0.1, 0.3, 0.2, 0.4],
    [0.4, 0.3, 0.1, 0.2]
]

# Compute AB
matrix_AB = []
for row_index in range(len(matrix_A)):
    new_row = []
    for col_index in range(len(matrix_B[0])):
        dot_product = sum(matrix_A[row_index][k] * matrix_B[k][col_index] for k in range(len(matrix_B)))
        new_row.append(dot_product)
    matrix_AB.append(new_row)

print("Matrix AB:")
for row in matrix_AB:
    #print each row of the resulting matrix to 2 decimal places
    print([f"{value:.2f}" for value in row])
