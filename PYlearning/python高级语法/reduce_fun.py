from functools import reduce


def is_add(x, y):
    return x + y


list_value = [1, 2, 3, 4, 5]
result = reduce(is_add, list_value)
print(result)
