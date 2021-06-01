rows, columns = [int(num) for num in input().split(", ")]

matrix = []
result = 0
for row in range(rows):
    matrix.append([int(num) for num in input().split(", ")])
    result += sum(matrix[row])

print(result)
print(matrix)