from collections import deque

rows, cols, = [int(el) for el in input().split(" ")]

string_queue = deque([el for el in input()])



matrix = []

for row in range(rows):
    matrix.append([])
    if row % 2 == 0:
        for col in range(cols):
            element = string_queue.popleft()
            matrix[row].append(element)
            string_queue.append(element)
    if row % 2 == 1:
        matrix[row] = deque()
        for col in range(cols, 0, -1):
            element = string_queue.popleft()
            matrix[row].appendleft(element)
            string_queue.append(element)

for row in range(len(matrix)):
    print("".join(matrix[row]))