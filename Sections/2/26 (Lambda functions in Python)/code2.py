def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [(lambda x: 2)(x) for x in sequence]
doulbed = list(map(lambda x: x * 2, sequence))