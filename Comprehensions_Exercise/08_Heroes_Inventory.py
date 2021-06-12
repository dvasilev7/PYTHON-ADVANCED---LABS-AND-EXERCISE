Inventory = {name: {} for name in input().split(", ")}

command = input()
while not command == "End":
    name, item, cost = command.split("-")
    cost = int(cost)
    if not item in Inventory[name]:
        Inventory[name][item] = cost
    command = input()

for name in Inventory:
    cost = sum(Inventory[name].values())
    count = len(Inventory[name])
    print(f"{name} -> Items: {count}, Cost: {cost}")