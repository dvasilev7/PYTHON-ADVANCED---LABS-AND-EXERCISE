from collections import deque


males = [int(num) for num in input().split()]
females = deque()
[females.append(int(num)) for num in input().split()]

matchesCount = 0

while males and females:
    male = males[-1]
    female = females[0]
    if male <= 0:
        males.pop()
        continue
    elif female <= 0:
        females.popleft()
        continue
    elif male % 25 == 0:
        males.pop()
        continue
    elif female % 25 == 0:
        females.popleft()
        continue
    if male == female:
        males.pop()
        females.popleft()
        matchesCount += 1
    else:
        females.popleft()
        males[-1] -= 2

males = males[::-1]

print(f"Matches: {matchesCount}")
if males:
    print("Males left:", ", ".join([str(male) for male in males]))
else:
    print("Males left: none")
if females:
    print("Females left:", ", ".join([str(female) for female in females]))
else:
    print("Females left: none")