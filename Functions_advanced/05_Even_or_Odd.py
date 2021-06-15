def odd_or_even(cmnd_, nums):
    num_sum = 0
    if cmnd_ == "Odd":
        num_sum = sum(list(filter(lambda x: x % 2 == 1, nums)))
    if cmnd_ == "Even":
        num_sum = sum(list(filter(lambda x: x % 2 == 0, nums)))
    return num_sum * len(nums)


command = input()
numbers = [int(num) for num in input().split()]

print(odd_or_even(command, numbers))