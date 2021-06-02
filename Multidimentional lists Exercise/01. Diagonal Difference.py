n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split(" ")])

prime_diagonal_sum = 0
sec_diagonal_sum = 0

for row in range(n):
    for col in range(n):
        if row == col:
            prime_diagonal_sum += matrix[row][col]

row_counter = n - 1
for row in range(n):
    for col in range(n - 1, -1, -1):
        if row_counter == col:
            sec_diagonal_sum += matrix[row][col]
    row_counter -= 1

difference = abs(prime_diagonal_sum - sec_diagonal_sum)

print(difference)