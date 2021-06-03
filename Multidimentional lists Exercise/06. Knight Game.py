n = int(input())

board = []

for row in range(n):
    board.append([])
    [board[row].append(el) for el in input()]


def knight_attack(matrix):
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                positions_to_check = [
                    (row - 1, col - 2),
                    (row + 1, col + 2),
                    (row - 1, col + 2),
                    (row + 1, col - 2),
                    (row - 2, col - 1),
                    (row - 2, col + 1),
                    (row + 2, col + 1),
                    (row + 2, col - 1)
                ]
                for position in range(len(positions_to_check)):
                    pos_row, pos_col = positions_to_check[position]
                    if not 0 <= pos_row <= n - 1:
                        continue
                    if not 0 <= pos_col <= n - 1:
                        continue
                    if matrix[pos_row][pos_col] == "K":
                        return True
    return False


def calculate_aggression(matrix):
    aggression_scores = {}
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                positions_to_check = [
                    (row - 1, col - 2),
                    (row + 1, col + 2),
                    (row - 1, col + 2),
                    (row + 1, col - 2),
                    (row - 2, col - 1),
                    (row - 2, col + 1),
                    (row + 2, col + 1),
                    (row + 2, col - 1)
                ]
                attacked_count = 0
                for position in range(len(positions_to_check)):
                    pos_row, pos_col = positions_to_check[position]
                    if not 0 <= pos_row <= n - 1:
                        continue
                    if not 0 <= pos_col <= n - 1:
                        continue
                    if matrix[pos_row][pos_col] == "K":
                        attacked_count += 1
                aggression_scores[(row, col)] = attacked_count
    return aggression_scores


def find_max_aggression(agro_dict):
    max_agro = 0
    for pos, agro in agro_dict.items():
        if agro > max_agro:
            max_agro = agro
            index_r, index_c = pos
    return index_r, index_c


moves_count = 0
is_attacked = knight_attack(board)
while is_attacked:
    aggression_dict = calculate_aggression(board)
    r, c = find_max_aggression(aggression_dict)
    board[r][c] = "0"
    moves_count += 1
    is_attacked = knight_attack(board)

print(moves_count)
