n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split(" ")])


indexes = input().split(" ")

for i in range(len(indexes)):
    row, column = [int(el) for el in indexes[i].split(",")]
    bomb = matrix[row][column]
    positions = [(0, 0), (0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1)]
    if bomb > 0:
        for position in positions:
            pos_row, pos_col = position
            if not 0 <= row + pos_row <= n - 1:
                continue
            if not 0 <= column + pos_col <= n - 1:
                continue
            if matrix[row + pos_row][column + pos_col] > 0:
                matrix[row + pos_row][column + pos_col] -= bomb
            else:
                continue
    else:
        continue

alive_count = 0
alive_sum = 0
for row in range(n):
    for column in range(n):
        if matrix[row][column] > 0:
            alive_count += 1
            alive_sum += matrix[row][column]

print(f"Alive cells: {alive_count}")
print(f"Sum: {alive_sum}")
for row in range(n):
    print(" ".join([str(el) for el in matrix[row]]))