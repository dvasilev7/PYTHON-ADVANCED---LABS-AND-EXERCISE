from collections import deque

players = deque(input().split(", "))
player_1, player_2 = players

matrix = [input().split() for row in range(7)]

score = {player_1: 501, player_2: 501}
throws = {player_1: 0, player_2: 0}

while len(players) == 2:
    row, col = [int(num) for num in input()[1:-1]. split(", ")]
    player = players.popleft()
    throws[player] += 1
    if row < 0 or row >= 7 or col < 0 or col >= 7:
        players.append(player)
        continue
    if matrix[row][col].isnumeric():
        score[player] -= int(matrix[row][col])
    elif matrix[row][col] == "D":
        score[player] -= 2 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
    elif matrix[row][col] == "T":
        score[player] -= 3 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
    elif matrix[row][col] == "B":
        score[player] -= score[player]
    if score[player] <= 0:
        print(f"{player} won the game with {throws[player]} throws!")
        break
    else:
        players.append(player)