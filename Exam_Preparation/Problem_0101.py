from collections import deque

orders = deque(int(num) for num in input().split(", "))
employees = [int(num) for num in input().split(", ")]

pizzas = 0
while orders:
    if not employees:
        break
    current_order = orders.popleft()
    employee = employees.pop()
    if 0 >= current_order or current_order > 10:
        employees.append(employee)
        continue
    if employee >= current_order:
        pizzas += current_order
        continue
    else:
        pizzas += employee
        orders.appendleft(current_order - employee)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas}")
    print("Employees:", ', '.join([str(emp) for emp in employees]))
else:
    print("Not all orders are completed.")
    print("Orders left:", ', '.join([str(order) for order in orders]))