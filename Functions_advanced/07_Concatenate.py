from functools import reduce


def concatenate(*args):
    return reduce(lambda x, y: x + y, args)
