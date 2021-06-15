def is_even(num):
    return num % 2 ==0

print(list(filter(is_even, [int(num) for num in input().split()])))