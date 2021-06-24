def stock_availability(cupcakes, command, *args):
    if command == "delivery":
        for el in args:
            cupcakes.append(el)
    elif command == "sell":
        if not args:
            cupcakes.remove(cupcakes[0])
        else:
            for par in args:
                if type(par) == int:
                    from collections import deque
                    cupcakes_queue = deque()
                    [cupcakes_queue.append(el) for el in cupcakes]
                    for cup in range(par):
                        cupcakes_queue.popleft()
                    cupcakes = list(cupcakes_queue)
                else:
                    if par in cupcakes:
                        cupcakes = list(filter(lambda x: x != par, cupcakes))
    return cupcakes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))




