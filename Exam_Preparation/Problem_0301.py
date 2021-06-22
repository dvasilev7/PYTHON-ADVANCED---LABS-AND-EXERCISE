def flights(*args):
    flights_list = args
    flights_dict = {}
    for fl in range(0, len(flights_list), 2):
        command = flights_list[fl]
        if command != "Finish":
            passengers_count = flights_list[fl + 1]
            if command in flights_dict:
                flights_dict[command] += passengers_count
            else:
                flights_dict[command] = passengers_count
        else:
            break
    return flights_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))