from math import floor
size = int(input())

matrix = [[el for el in input().split()] for row in range(size)]

player = [0, 0]
walls = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player = [row, col]
        if matrix[row][col] == "X":
            walls.append([row, col])

path = []
coins = 0
while coins < 100:
    command = input()
    if command == "up":
        player[0] -= 1
    elif command == "down":
        player[0] += 1
    elif command == "left":
        player[1] -= 1
    elif command == "right":
        player[1] += 1
    if player[0] < 0 or player[0] > size - 1 or player[1] < 0 or player[1] > size - 1 or player in walls:
        coins *= 0.5
        break
    else:
        coins += int(matrix[player[0]][player[1]])
        path.append(tuple(player))


total_coins = floor(coins)
if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
path = [list(t) for t in path]
print("Your path:")
[print(point) for point in path]


