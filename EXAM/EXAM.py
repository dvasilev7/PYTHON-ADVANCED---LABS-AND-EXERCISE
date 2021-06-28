from collections import deque

chocolates = [int(num) for num in input().split(", ")]
cups_milk = deque(int(num) for num in input().split(", "))

milkshakes = 0

while chocolates and cups_milk:
    current_choc = chocolates[-1]
    current_cup = cups_milk[0]
    if current_choc <= 0 and current_cup <= 0:
        chocolates.pop()
        cups_milk.popleft()
        continue
    if current_choc <= 0:
        chocolates.pop()
        continue
    elif current_cup <= 0:
        cups_milk.popleft()
        continue
    if current_cup == current_choc:
        chocolates.pop()
        cups_milk.popleft()
        milkshakes += 1
    else:
        cups_milk.rotate(-1)
        chocolates[-1] -= 5
    if milkshakes == 5:
        break


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print("Chocolate:", ", ".join([str(num) for num in chocolates]))
else:
    print("Chocolate: empty")
if cups_milk:
    print("Milk:", ", ".join([str(num) for num in cups_milk]))
else:
    print("Milk: empty")