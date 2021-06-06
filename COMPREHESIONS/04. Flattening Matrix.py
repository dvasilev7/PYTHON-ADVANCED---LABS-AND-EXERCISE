n = int(input())

nums = [[int(el) for el in input().split(", ")]for _ in range(n)]
flatt_nums = [num for sublist in nums for num in sublist]


print(flatt_nums)
