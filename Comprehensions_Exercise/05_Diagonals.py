n = int(input())

matrix = [[int(number) for number in input().split(", ")] for row in range(n)]

first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n-1-i] for i in range(n)]

print(f'First diagonal: {", ".join([str(i) for i in first_diagonal])}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join([str(i) for i in second_diagonal])}. Sum: {sum(second_diagonal)}')