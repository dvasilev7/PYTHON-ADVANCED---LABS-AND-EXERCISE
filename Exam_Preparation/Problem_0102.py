from collections import deque

effects = deque(int(num) for num in input().split(", "))
stack_power = [int(num) for num in input().split(", ")]

palm = 0
willow = 0
cross = 0
while effects:
    effect = effects.popleft()
    power = stack_power.pop()
    reaction = effect + power
    if effect <= 0:
        stack_power.append(power)
        continue
    elif power <= 0:
        effects.appendleft(effect)
        continue
    if reaction % 3 == 0 and reaction % 5 != 0:
        palm += 1
    elif reaction % 3 != 0 and reaction % 5 == 0:
        willow += 1
    elif reaction % 3 == 0 and reaction % 5 == 0:
        cross += 1
    else:
        effect -= 1
        effects.append(effect)
        stack_power.append(power)
    if palm >= 3 and willow >= 3 and cross >= 3:
        print("Congrats! You made the perfect firework show!")
        break

if palm < 3 or willow < 3 or cross < 3:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print("Firework Effects left:", ", ".join([str(ef) for ef in effects]))
if stack_power:
    print("Explosive Power left:", ", ".join([str(p) for p in stack_power]))
print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {cross}")
