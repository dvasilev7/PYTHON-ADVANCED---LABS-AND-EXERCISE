rows, cols, = [int(el) for el in input().split(" ")]

matrix = []

for row in range(rows):
    matrix.append([el for el in input().split(" ")])

is_valid = False

command = input()
while command != "END":
    command_list = command.split()
    if len(command_list) == 5:
        action = command_list[0]
        row1 = int(command_list[1])
        col1 = int(command_list[2])
        row2 = int(command_list[3])
        col2 = int(command_list[4])
        if action == "swap" and rows > row1 and rows > row2 and col1 < cols and col2 < cols:
            is_valid = True
        else:
            is_valid = False
    if is_valid:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in range(len(matrix)):
            print(" ".join(matrix[row]))
    else:
        print("Invalid input!")

    command = input()
