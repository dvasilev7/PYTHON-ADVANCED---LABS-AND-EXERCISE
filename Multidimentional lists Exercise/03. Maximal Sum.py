from sys import maxsize


def max_3x3(m, rs, cs):
    current_sum = 0
    matrix_3x3 = []
    counter = -1
    for r in range(rs, rs + 3):
        matrix_3x3.append([])
        counter += 1
        for c in range(cs, cs + 3):
            matrix_3x3[counter].append(m[r][c])
            current_sum += int(m[r][c])
    return matrix_3x3, current_sum


rows, cols = [int(el) for el in input().split(" ")]

matrix = []

for row in range(rows):
    matrix.append([el for el in input().split(" ")])


maximum = - maxsize
max_matrix = None

for row in range(rows - 2):
    for col in range(cols - 2):
        matrix_3x3, current_sum = max_3x3(matrix, row, col)
        if current_sum >= maximum:
            maximum = current_sum
            max_matrix = matrix_3x3

print(f"Sum = {maximum}")
print(" ".join(max_matrix[0]))
print(" ".join(max_matrix[1]))
print(" ".join(max_matrix[2]))