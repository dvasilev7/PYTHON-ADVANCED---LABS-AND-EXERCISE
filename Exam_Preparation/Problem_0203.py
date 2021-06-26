text = [el for el in input()]
n = int(input())
matrix = [[el for el in input()] for row in range(n)]
m = int(input())

current_position = [0, 0]

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            current_position = row, col

srow, scol = current_position
matrix[srow][scol] = "-"

for c in range(m):
    command = input()
    row, col = current_position
    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "right":
        col += 1
    elif command == "left":
        col -= 1
    if row < 0 or row >= n or col < 0 or col >= n:
        if text:
            text.pop()
    else:
        if matrix[row][col].isalpha():
            text.append(matrix[row][col])
            matrix[row][col] = "-"
        current_position = row, col

frow, fcol = current_position
matrix[frow][fcol] = "P"

print("".join(text))
[print("".join([el for el in row]))for row in matrix]