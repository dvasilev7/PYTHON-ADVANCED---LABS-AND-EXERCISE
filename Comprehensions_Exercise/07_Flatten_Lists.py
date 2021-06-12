matrix = [
    [el for el in sub.split()]
    for sub in input().split("|")
]
matrix.reverse()
list_flat = [num for sublist in matrix for num in sublist]
print(" ".join(list_flat))