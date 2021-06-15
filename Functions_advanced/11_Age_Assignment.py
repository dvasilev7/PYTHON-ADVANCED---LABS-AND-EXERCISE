def age_assignment(*args, **kwargs):
    age_dict = {}
    for name in args:
        for key, value in kwargs.items():
            if key[0] == name[0]:
                age_dict[name] = value
    return age_dict


print(age_assignment("Peter", "George", G=26, P=19))