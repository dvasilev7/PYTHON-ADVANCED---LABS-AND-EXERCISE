def creator_chr(row, col):
    base = ord("a")

    first_letter = chr(row + base)
    middle_letter = chr(col + row + base)
    return f"{first_letter}{middle_letter}{first_letter}"


r, c = [int(num) for num in input().split(" ")]

matrix = [[creator_chr(row, col) for col in range(c)]for row in range(r)]


[print(" ".join([el for el in matrix[row]])) for row in range(r)]