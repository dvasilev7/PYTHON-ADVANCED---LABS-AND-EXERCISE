def get_magic_triangle(integer):
    matrix = []
    for row in range(integer):
        matrix.append([1 for el in range(row + 1)])
    for row in range(integer):
        for col in range(row+1):
            if 0 < col < row:
                matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
    return matrix


print(get_magic_triangle(5))