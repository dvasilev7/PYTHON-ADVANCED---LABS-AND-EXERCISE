def even_odd(*args):
    nums = args[0:-1]
    command = args[len(args) - 1]
    if command == "odd":
        nums = list(filter(lambda x: x % 2 == 1, nums))
    if command == "even":
        nums = list(filter(lambda x: x % 2 == 0, nums))
    return nums


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))